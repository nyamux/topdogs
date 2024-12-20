const express = require('express');
const router = express.Router();
const User = require('../models/User');


// Add this to routes/auth.js
router.get('/status', (req, res) => {
    res.json({
        isLoggedIn: !!req.session.user,
        user: req.session.user ? {
            username: req.session.user.username
        } : null
    });
});
// Login route
router.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ msg: 'Invalid credentials' });
        }

        const isMatch = password === user.password; // For testing purposes
        if (!isMatch) {
            return res.status(400).json({ msg: 'Invalid credentials' });
        }

        req.session.user = {
            id: user._id,
            username: user.username
        };
        
        res.json({ msg: 'Logged in successfully' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ msg: 'Server error' });
    }
});

// Logout route
router.get('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            return res.status(500).json({ msg: 'Error logging out' });
        }
        res.redirect('/login.html');
    });
});

module.exports = router;