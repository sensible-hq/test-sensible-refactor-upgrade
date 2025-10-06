---
title: Page range
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Ignores pages outside the start page and end page.

**Note**: To configure a page range on a field-by-field basis for LLM-based methods, see each method's Page Range parameter.

Parameters
----

<table>
  <thead>
    <tr>
      <th>key</th>
      <th>value</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>type</td>
      <td><code>pageRange</code></td>
      <td></td>
    </tr>
    <tr>
      <td>startPage</td>
      <td>number. default: 0</td>
      <td>Zero-based index of the first page (inclusive).</td>
    </tr>
    <tr>
      <td>endPage</td>
      <td>number. default: last page</td>
      <td>Zero-based index of the last page (exclusive).</td>
    </tr>
  </tbody>
</table>