# 🌐 API Requests (Fetch API)

## 🎯 **Fetching Data**

> [!SUCCESS] **Definition**: Getting data from an external server (JSON).
> Powered by the `fetch()` function (Built-in).

---

## 📨 **The Fetch Flow**

1.  Call `fetch(url)`. Returns a Promise.
2.  Wait for **Response Object** (Headers, Status).
3.  Convert Body to JSON (`.json()`). Returns another Promise.
4.  Get Data.

```javascript
async function loadUsers() {
    try {
        const response = await fetch('https://api.example.com/users');
        
        // Check if status is OK (200-299)
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json(); // Read body stream
        console.log(data);
    } catch (err) {
        console.log("Network logic failed:", err);
    }
}
```

---

## 📤 **Sending Data (POST)**

> Add an options object as the second argument.

```javascript
fetch('url', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: "Alice" }) // Convert JS Obj to String
});
```

---

## 🧠 **Memory Tricks**

> [!NOTE] **Remember This!** 🧠
> - **Twice Await**: Wait for Server ➡️ Wait for JSON parsing.
> - **Check OK**: Fetch doesn't reject on 404/500 errors! You MUST check `response.ok`.
> - **Stringify Body**: You can't send raw JS objects. Wrap 'em! 📦

---

## ❓ **5 Questions to Test Yourself**

> [!QUESTION] **Q1**: How many promises are usually involved in a JSON fetch?
> > [!SUCCESS]- Answer
> > Two. One for the network response, one for parsing the JSON body.

> [!QUESTION] **Q2**: If specific website returns a 404 (Not Found), does fetch throw an error?
> > [!SUCCESS]- Answer
> > **No!** It resolves successfully. You must manually check `response.ok` or `response.status`.

> [!QUESTION] **Q3**: What method converts the response body into a JavaScript object?
> > [!SUCCESS]- Answer
> > `.json()`.

> [!QUESTION] **Q4**: What header is essential when sending JSON data?
> > [!SUCCESS]- Answer
> > `'Content-Type': 'application/json'`.

> [!QUESTION] **Q5**: What is the default HTTP method for fetch?
> > [!SUCCESS]- Answer
> > `GET`.

---

Back to: [[Sem Exam/Frontend-Dev/Module 12 - Async JS/README|Module 12 Hub]] | [[frontend-Sem-Hub|Sem Exam Hub]]
