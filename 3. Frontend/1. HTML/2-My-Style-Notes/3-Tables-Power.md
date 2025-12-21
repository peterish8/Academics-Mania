# 📊 Tables Power - My Style Notes

## 🎯 **What are Tables?**

> [!INFO] **Definition**: Display data in structured rows and columns
> Like **Excel spreadsheets** but in HTML! 📈

**📍 Key Points:**
- Organize data in rows and columns
- Perfect for structured information
- Each cell can hold different content
- Essential for data comparison

**🎯 Use Cases:**
- Student grade sheets
- Product price comparisons
- Employee records
- Sports statistics
- Financial reports

---

## 🏗️ **Table Structure**

> [!INFO] **Definition**: Tables have a specific hierarchy of elements
> Think of it as **building blocks**!

**📍 Key Elements:**
- `<table>` - The container (like Excel file)
- `<tr>` - Table row (horizontal line)
- `<td>` - Table data (individual cell)
- `<th>` - Table header (bold column titles)

**🎨 Visual:**
```
<table>           ← The spreadsheet
  <tr>            ← Row 1 (horizontal)
    <th>Name</th> ← Header cell (bold)
    <th>Age</th>  ← Header cell (bold)
  </tr>
  <tr>            ← Row 2 (horizontal)
    <td>John</td> ← Data cell
    <td>25</td>   ← Data cell
  </tr>
</table>
```

**🎯 Use Cases:**
- `<table>` - Wrap everything
- `<tr>` - Each row of data
- `<th>` - Column headers (bold)
- `<td>` - Regular data cells

---

## 🏷️ **Table Sections**

> [!INFO] **Definition**: Organize table into logical sections
> Like **header, body, footer** of a document!

**📍 Key Sections:**
- `<thead>` - Header section (column titles)
- `<tbody>` - Body section (main data)
- `<tfoot>` - Footer section (totals, summaries)
- `<caption>` - Table title/description

**🎨 Visual:**
```
<table>
  <caption>Student Grades</caption>  ← Table title
  <thead>                           ← Header section
    <tr><th>Name</th><th>Grade</th></tr>
  </thead>
  <tbody>                           ← Body section
    <tr><td>Alice</td><td>95</td></tr>
    <tr><td>Bob</td><td>87</td></tr>
  </tbody>
  <tfoot>                           ← Footer section
    <tr><td>Average</td><td>91</td></tr>
  </tfoot>
</table>
```

**🎯 Use Cases:**
- `<thead>` - Column headers
- `<tbody>` - Main data rows
- `<tfoot>` - Totals, averages
- `<caption>` - Table description

---

## 🔗 **Cell Merging**

> [!INFO] **Definition**: Make cells span multiple columns or rows
> Like **merging cells in Excel**!

**📍 Key Attributes:**
- `colspan` - Span multiple columns (horizontal →)
- `rowspan` - Span multiple rows (vertical ↓)
- Number = how many cells to merge

**🎨 Visual:**
```
colspan="2" → [    Cell spans 2 columns    ]
                    ↑              ↑
                 col 1           col 2

rowspan="2" → [ Cell  ]
              [ spans ]
              [ 2 rows]
                ↑
              row 1
                ↑  
              row 2
```

**🎯 Use Cases:**
- `colspan` - Category headers spanning multiple columns
- `rowspan` - Labels spanning multiple rows
- Combined data grouping

---

## ⚙️ **Table Attributes**

> [!INFO] **Definition**: Control table appearance and behavior
> Add **styling and structure**!

**📍 Key Attributes:**
- `border` - Add borders around cells
- `width` - Set table width
- `cellpadding` - Space inside cells
- `align` - Align content in cells

**🎨 Visual:**
```
border="1"     → ┌─────┬─────┐
                 │ A   │ B   │
                 ├─────┼─────┤
                 │ C   │ D   │
                 └─────┴─────┘

cellpadding="10" → │  text  │ (more space)
cellpadding="2"  → │text│     (less space)
```

**🎯 Use Cases:**
- `border="1"` - Visible table lines
- `width="100%"` - Full page width
- `cellpadding="10"` - Comfortable spacing
- `align="center"` - Center content

---

## 🎨 **Real Examples**

### **📚 Student Grades**
```html
<table border="1">
    <caption>🎓 Class Results</caption>
    <thead>
        <tr>
            <th>Student</th>
            <th>Math</th>
            <th>Science</th>
            <th>Total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>95</td>
            <td>88</td>
            <td>183</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>87</td>
            <td>92</td>
            <td>179</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td><strong>Average</strong></td>
            <td>91</td>
            <td>90</td>
            <td>181</td>
        </tr>
    </tfoot>
</table>
```

### **💰 Pricing Comparison**
```html
<table border="1">
    <thead>
        <tr>
            <th>Plan</th>
            <th>Price</th>
            <th>Features</th>
            <th>Support</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Basic</td>
            <td>$9/month</td>
            <td>5 projects</td>
            <td>Email</td>
        </tr>
        <tr>
            <td>Pro</td>
            <td>$19/month</td>
            <td>Unlimited</td>
            <td>24/7 Chat</td>
        </tr>
    </tbody>
</table>
```

### **🔗 Merged Cells Example**
```html
<table border="1">
    <tr>
        <th colspan="3">🏢 Company Information</th>
    </tr>
    <tr>
        <td rowspan="2">Contact</td>
        <td>Email</td>
        <td>info@company.com</td>
    </tr>
    <tr>
        <td>Phone</td>
        <td>+1-234-567-8900</td>
    </tr>
</table>
```

### **📊 Sales Report**
```html
<table border="1" width="100%">
    <caption>📈 Q1 Sales Report</caption>
    <thead>
        <tr>
            <th>Month</th>
            <th>Revenue</th>
            <th>Growth</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>January</td>
            <td>$50,000</td>
            <td>+5%</td>
        </tr>
        <tr>
            <td>February</td>
            <td>$55,000</td>
            <td>+10%</td>
        </tr>
        <tr>
            <td>March</td>
            <td>$60,000</td>
            <td>+9%</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td><strong>Total</strong></td>
            <td><strong>$165,000</strong></td>
            <td><strong>+8%</strong></td>
        </tr>
    </tfoot>
</table>
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Table Hierarchy** 🏗️
> ```
> table (house)
>   └── tr (floors)
>       └── td/th (rooms)
> ```

> [!TIP] **Quick Checklist** ✅
> 1. Start with `<table>`
> 2. Add `<tr>` for each row
> 3. Add `<td>` for data, `<th>` for headers
> 4. Use `<thead>`, `<tbody>` for organization

> [!SUCCESS] **Memory Aids** 🧠
> - **tr** = **T**able **R**ow (horizontal line)
> - **td** = **T**able **D**ata (regular cell)
> - **th** = **T**able **H**eader (bold cell)
> - **colspan** = **col**umns (horizontal →)
> - **rowspan** = **row**s (vertical ↓)

Back to: [[README of HTML]]