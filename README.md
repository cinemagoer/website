The site uses the [Lektor](https://www.getlektor.com/) static site generator.

## Installation

Install the necessary packages:

```
pip install lektor
```

- Start the live development server:

  ```
  lektor server
  ```

- Browse to the reported URL.

- Edit the files and see the results in the browser.

- When you're done, push your changes and the site will be automatically
  built and deployed.

- To build or deploy manually, run the commands:

  ```
  lektor build
  lektor deploy ghpages
  ```

## Content

The site content is under the `content` directory.
There is one directory per page.
The content of the page is placed into the `contents.lr` file
in the corresponding directory.

News items have to be placed into the `news` directory.

The `ecosystem` page consists of `project` elements.

## Style

The stylesheet is `assets/static/main.css`.

## Content Modeling

Fields of content types (like news items and projects) are stored
in `.ini` files under the `models` directory.

For each content type, there has to be a template
under the `templates` directory.

Templates can use data stored in `.json` files under the `databags` directory.
