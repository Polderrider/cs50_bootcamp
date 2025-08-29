from pathlib import Path


def list_entries():
    """ returns a list of the names of all 
        encyclopedia entries currently saved 
    """

    """ 
     Notes: 
     .resolve(). will return an absolute path. If the path is already absolute the method will have no effect. https://stackoverflow.com/questions/76451315/difference-between-pathlib-path-resolve-and-pathlib-path-parent
     .glob('pattern') finds all the pathnames matching a specified pattern https://docs.python.org/3/library/glob.html
       """
    here = Path(__file__).resolve().parent
    rootdir = here / "entries"
    return [f.stem for f in rootdir.glob("*.md")]
    
    # region list_entries() debugging script
    # """Return names (without extension) of all .md files in entries/ one level up."""
    # here = Path(__file__).resolve().parent
    # rootdir = here / "entries"

    # if debug:
    #     print(f"[DEBUG] util.py directory: {here}")
    #     print(f"[DEBUG] entries path:     {rootdir}")
    #     print(f"[DEBUG] entries exists:   {rootdir.exists()}  is_dir: {rootdir.is_dir()}")
    #     if rootdir.exists():
    #         try:
    #             print("[DEBUG] entries contents:", [p.name for p in rootdir.iterdir()])
    #         except Exception as e:
    #             print(f"[DEBUG] iterdir() error: {e!r}")

    # # Be robust to .MD/.Md/.mD etc and ignore non-files
    # return [
    #     p.stem
    #     for p in (rootdir.iterdir() if rootdir.exists() else [])
    #     if p.is_file() and p.suffix.lower() == ".md"
    # ]
    # endregion
    
        
def get_entry(title):
    """ returns an encyclopedia entry by its 
        title, returning its Markdown contents 
        if the entry exists or None if the entry does not exist 
      """
    
    # access md files in entries folder
    here = Path(__file__).resolve().parent # returns this file's absolute path
    rootdir = here / "entries"  # enters entries folder 
    md_file = rootdir/f'{title}.md'

    if not md_file.exists():
        raise FileNotFoundError(f"No entry found: {md_file}")

    # read md_file into variable
    md_data = md_file.read_text(encoding="utf-8")
    
    return md_data

    # convert md_file data into html
    # return html data to view




def save_entry(title, md_file):
    """ saves a new encyclopedia entry, given 
        its title and some Markdown content  
    """
    pass





