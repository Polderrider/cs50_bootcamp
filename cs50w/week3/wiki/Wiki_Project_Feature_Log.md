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
| 8.0        | Edit Page View               | Display a form pre-filled with current Markdown for editing an existing entry                |
| 8.1        | Edit Page Save Logic         | Save edited content and redirect back to updated entry page                                  |
| 8.2        | Edit Link on Entry Page      | Add a link to each entry page to access the edit form                                        |
| 9.0        | Delete functionality         | add delete button to edit page; move .md file to a folder named trash                        |
| 10        | Random Entry View             | Create view to redirect to a random entry                                                    |

| 11      | rename page form               | Separate from edit—accept existing title and a new title to rename the file.                     | case-insensitivity and duplicate checks.




| 12      | Search Filter form             | Add dropdowns/radios to filter results (e.g. “Starts with…”, “Contains…”, “Ends with…”)           | text input and select/radio fields
| 13      | Export Page Form               | Pick a page from a dropdown, choose export format (Markdown, HTML, plain text), and then render it in the browser.    |
| 14.     | add flash messages.            |                          |


| XX      | next feature name            | description                                               |


| 21        | HTML Validator Integration   | Use HTML validator to check rendered html templates to catch invalid nesting and markup early |
| 22        | add.html UI                  | add markdown guide for user                                                                    |



---

## Usage

- Work through features sequentially.
- Each feature should live on its own branch.
- Merge into `main` only when feature is complete and tested.

”