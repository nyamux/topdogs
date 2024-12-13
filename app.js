// Step 1: Create a simple Node.js application
const express = require('express');
const session = require('express-session');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Store valid usernames and passwords
const users = {
    "mombasa": "jE5r!;",
    "kwale": "Rp.8EC",
    "kilifi": "a<H5XD",
    "tana river": "sK-e2W",
    "lamu": "Gt7)u$",
    "taita taveta": "Vv;3hz",
    "garissa": "H7`c4B",
    "wajir": "bP5E`C",
    "mandera": "B$g5q.",
    "marsabit": "q^)U5E",
    "isiolo": "K$[t5?",
    "meru": "pT%4:A",
    "tharaka-nithi": "w4M!#H",
    "embu": "kS8_td",
    "kitui": "p7!^R$",
    "machakos": "w@QX9;",
    "makueni": "y4#uV2",
    "nyandarua": "wTm'9P",
    "nyeri": "b9Tn=.",
    "kirinyaga": "N*s9jL",
    "murang'a": "F57k#Z",
    "kiambu": "\"a+T\"\"2]\"",
    "turkana": "c9WA+(",
    "west pokot": "B8u`-E",
    "samburu": "R]8y7D",
    "trans-nzoia": "xZ%5w+",
    "uasin gishu": "B7d^vL",
    "elgeyo-marakwet": "c8E-g=",
    "nandi": "H3Qb)G",
    "baringo": "Dg=Q9(",
    "laikipia": "\"Ac5&,6\"",
    "nakuru": "dc2[Uw",
    "narok": "m{4eJF",
    "kajiado": "kG5<wj",
    "kericho": "t9~sL&",
    "bomet": "DB6u`;",
    "kakamega": "h3W$fp",
    "vihiga": "Ry*?8D",
    "bungoma": "e}7Myk",
    "busia": "zt5'Pu",
    "siaya": "m6_7YE",
    "kisumu": "j'x5Z;",
    "homa bay": "Kyg8#*",
    "migori": "r7JV/8",
    "kisii": "v;G_3x",
    "nyamira": "r4`=X>",
    "nairobi": "at:9ZF",
    "diaspora": "h}U2Na",
};

// Middleware for session handling
app.use(session({
    secret: 'secure-secret',
    resave: false,
    saveUninitialized: true
}));

// Middleware for parsing form data
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    if (req.session.loggedIn) {
        const htmlContent = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
        res.send(htmlContent);
    } else {
        res.redirect('/login');
    }
});

app.get('/login', (req, res) => {
    res.send(`<form method='POST' action='/login'>
                <label>Username: <input type='text' name='username'/></label><br>
                <label>Password: <input type='password' name='password'/></label><br>
                <button type='submit'>Login</button>
              </form>`);
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (users[username] === password) {
        req.session.loggedIn = true;
        req.session.username = username;
        res.redirect('/');
    } else {
        res.send('<h1>Login failed</h1><br><a href="/login">Try again</a>');
    }
});

app.get('/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/login');
});

// Start server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
