# Wiki Project — Feature Log

This log tracks the incremental features for the Wiki project (CS50W — Project 1).  
Each feature should be developed on its own git branch before merging into main.

---

## Feature Log

| Feature # | Feature Name                 | Description                                                                                  |
|-----------|------------------------------|----------------------------------------------------------------------------------------------|
| 1         | Project Setup                | Initialize Django project and app, create required folders and basic templates               |
| 2         | Index View                   | Render the index page with a list of encyclopedia entries (static placeholder list for now)  |
| 3         | Entry Markdown Storage       | Store each entry as a Markdown (.md) file in a local `entries/` folder                       |
| 3         | Entry Markdown Retrieval     | Implement function to retrieve the Markdown content of an entry by title                     |
| 3         | Markdown to HTML Conversion  | Convert Markdown to HTML before rendering entry pages                                        |
| 3         | Entry Page View              | Create a dynamic route `/wiki/<title>` to display a specific entry                           |
| 3         | Entry Not Found Page         | Display error page when a requested entry does not exist                                     |
| 4         | Tests                        | Create tests for project
| 5         | Index Page Link Integration  | Turn each index page list entry into a link to its respective entry page                     |
| 5.1       | Return to Index Page Links   | link wikipage back to the index page                    |
| 6         | Search Bar Form              | Add a working search form in the sidebar                                                     |
| 6         | Exact Match Search Redirect  | Redirect to entry page if user search query matches an entry title exactly                   |
| 6         | Partial Match Search Results | Display a search results page with entries containing the search substring                   |
| 6         | Search Results Linking       | Make each result entry on the search page link to the correct entry                          |
| 7.0        | New Page Form View           | Create a form to add new pages, including title and Markdown textarea                        |
| 7.1        | New Page Submission Logic    | Save new entry only if title does not exist; otherwise show error page                       |
| 7.2        | New Page Redirect            | Redirect to new entry page after saving a valid new page                                     |



| 16        | Edit Page View               | Display a form pre-filled with current Markdown for editing an existing entry                |
| 17        | Edit Page Save Logic         | Save edited content and redirect back to updated entry page                                  |
| 18        | Edit Link on Entry Page      | Add a link to each entry page to access the edit form                                        |
| 19        | Random Entry View            | Create view to redirect to a random entry                                                    |
| 20        | Random Page Link             | Add working “Random Page” link in sidebar                                                    |
| 21        | HTML Validator Integration   | Use HTML validator to check rendered html templates to catch invalid nesting and markup early |


---

## Usage

- Work through features sequentially.
- Each feature should live on its own branch.
- Merge into `main` only when feature is complete and tested.

”