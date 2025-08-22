from pathlib import Path

def list_entries():
    """ returns a list of the names of all 
        encyclopedia entries currently saved 
    """
    
    here = Path(__file__).resolve().parent          # Where is util.py? (absolute path)
    rootdir = here.parent / "entries"               # Step up one level, then into entries/
    return[f.stem for f in rootdir.glob("*.md")]    # use .suffix to access file type eg .md

    
    # Note: when looking through subfolders of entries/ with nested .md files inside, replace glob("*.md") for rglob("*.md"). r adds a recursive step to search subfolders




def save_entry(title, md_file):
    """ saves a new encyclopedia entry, given 
        its title and some Markdown content  
    """
    pass


def get_entry():
    """ returns an encyclopedia entry by its 
        title, returning its Markdown contents 
        if the entry exists or None if the entry does not exist 
      """
    pass




