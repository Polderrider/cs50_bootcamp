import re, html


class MiniMd():

    def __init__(self):

        # inline
        self.bold = re.compile(r'\*\*(.+?)\*\*')
        self.ital = re.compile(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)')
        self.code = re.compile(r'`([^`]+)`')
        self.link = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

        # block patterns across multilines
        self.h1 = re.compile(r'(?m)^\# (.+)$')
        self.h2 = re.compile(r'(?m)^\#\# (.+)$')
        self.h3 = re.compile(r'(?m)^\#\#\# (.+)$')
        self.ul = re.compile(r'(?m)^(?:- |\* )(.*)$')

    def convert(self, md: str) -> str:
        """ changes markdown input into equivalent html syntax 
        Compiling a pattern makes it more efficient when we need to use the same pattern several times"""

        # 0) Escape raw HTML first
        s = html.escape(md)

        # 1) Headings (block)
        s = self.h3.sub(r'<h3>\1</h3>', s)
        s = self.h2.sub(r'<h2>\1</h2>', s)
        s = self.h1.sub(r'<h1>\1</h1>', s)


        # 2) Lists (very naive: each list item to <li>, then wrap groups)
        s = self.ul.sub(r'<li>\1</li>', s)

        # Wrap consecutive <li>…</li> groups in <ul>…</ul>
        s = re.sub(r'(?:\n?(<li>.*?</li>))+', 
                   lambda m: '<ul>\n' + re.sub(r'^\n', '', m.group(0), flags=re.M) + '\n</ul>', s, flags=re.S)

        def para_wrap(text):
            parts = [p.strip() for p in re.split(r'\n\s*\n', text)]
            out = []
            for p in parts:
                if not p:
                    continue
                if re.match(r'^\s*<(h[1-6]|ul|ol|pre|blockquote)\b', p):
                    out.append(p)
                else:
                    out.append(f'<p>{p}</p>')
            return '\n\n'.join(out)

        s = para_wrap(s)

        # 4) Inline (order matters: code first so we don’t style inside code)
        s = self.code.sub(r'<code>\1</code>', s)
        s = self.bold.sub(r'<strong>\1</strong>', s)
        s = self.ital.sub(r'<em>\1</em>', s)
        s = self.link.sub(r'<a href="\2">\1</a>', s)

        return s


