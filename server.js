const express = require('express');
const session = require('express-session');
const connectDB = require('./config/db');
const User = require('./models/User');
const path = require('path');

const app = express();

// Connect Database
connectDB();

// Init Middleware
app.use(express.json());
app.use(express.static('public'));
app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: false
}));

// Authentication middleware
const auth = (req, res, next) => {
    if (!req.session.user) {
        return res.redirect('/login.html');
    }
    next();
};

// Serve login page as default
app.get('/', (req, res) => {
    if (!req.session.user) {
        res.redirect('/login.html');
    } else {
        res.sendFile(path.join(__dirname, 'public', 'index.html'));
    }
});

// Protect index.html
app.get('/index.html', auth, (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Routes
app.use('/api/auth', require('./routes/auth'));

// Initial user setup
const setupUsers = async () => {
    const credentials = [
        { username: 'Mombasa', password: 'jE5r!' },
        { username: 'Kwale', password: 'Rp.8EC' },
        { username: 'Kilifi', password: 'a<H5XD' },
        { username: 'Tana River', password: 'SK-e2W' },
        { username: 'Lamu', password: 'Gt7)u$' },
        { username: 'Taita Taveta', password: 'Vv;3hz' },
        { username: 'Garissa', password: 'H7 c4B' },
        { username: 'Wajir', password: 'bP5E C' },
        { username: 'Mandera', password: 'B$g5q.' },
        { username: 'Marsabit', password: 'q^)U5E' },
        { username: 'Isiolo', password: 'K$[t5?' },
        { username: 'Meru', password: 'PT%4:A' },
        { username: 'Tharaka-Nithi', password: 'w4M!#H' },
        { username: 'Embu', password: 'kS8 td' },
        { username: 'Kitui', password: 'p7!^R$' },
        { username: 'Machakos', password: 'w@QX9;' },
        { username: 'Makueni', password: 'y4#uV2' },
        { username: 'Nyandarua', password: 'wTm9P' },
        { username: 'Nyeri', password: 'b9Tn=.' },
        { username: 'Kirinyaga', password: 'N*s9jL' },
        { username: 'Murang\'a', password: 'F57k#Z' },
        { username: 'Kiambu', password: 'a+T"2]' },
        { username: 'Turkana', password: 'c9WA+(' },
        { username: 'West Pokot', password: 'B8u-E' },
        { username: 'Samburu', password: 'R]8y7D' },
        { username: 'Trans-Nzoia', password: 'xZ%5w+' },
        { username: 'Uasin Gishu', password: 'B7d^vL' },
        { username: 'Elgeyo-Marakwet', password: 'c8E-g=' },
        { username: 'Nandi', password: 'H3Qb)G' },
        { username: 'Baringo', password: 'Dg=Q9(' },
        { username: 'Laikipia', password: 'Ac5&,6' },
        { username: 'Nakuru', password: 'dc2[Uw' },
        { username: 'Narok', password: 'm{4eJF' },
        { username: 'Kajiado', password: 'kG5<wj' },
        { username: 'Kericho', password: 't9sL&' },
        { username: 'Bomet', password: 'DB6u;' },
        { username: 'Kakamega', password: 'h3W$fp' },
        { username: 'Vihiga', password: 'Ry*?8D' },
        { username: 'Bungoma', password: 'e}7Myk' },
        { username: 'Busia', password: 'zt5Pu' },
        { username: 'Siaya', password: 'm6_7YE' },
        { username: 'Kisumu', password: 'jx5Z;' },
        { username: 'Homa Bay', password: 'Kyg8#*' },
        { username: 'Migori', password: 'r7JV/8' },
        { username: 'Kisii', password: 'v;G_3x' },
        { username: 'Nyamira', password: 'r4`=X>' },
        { username: 'Nairobi', password: 'at:9ZF' },
        { username: 'Diaspora', password: 'h}U2Na' }
    ];

    try {
        for (const cred of credentials) {
            const userExists = await User.findOne({ username: cred.username });
            if (!userExists) {
                await User.create(cred);
            }
        }
        console.log('Users setup completed');
    } catch (err) {
        console.error('Error setting up users:', err);
    }
};

setupUsers();

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));