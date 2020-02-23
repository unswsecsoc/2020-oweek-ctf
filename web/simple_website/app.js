var express = require('express'),
	session = require('express-session'),
	fs = require('fs');

var port = process.env.PORT || 8000;

var app	= express();
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', './templates');
var path = require('path');
app.use(express.static(path.join(__dirname, '/public')));

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

var cookieParser = require('cookie-parser');
app.use(cookieParser());

function checkAdmin(req, res, next) {
	if (req.cookies['admin'] == 'true') {
		res.cookie('flag3/4', '3b5ite_i');
	}
	next();
}

app.get('/', checkAdmin, function(req, res) {
	if (req.cookies['admin'] === undefined || req.cookies['admin'] === null) {
		res.cookie('admin', false);
		res.clearCookie('flag3/4');
		res.clearCookie('user');
	} else if (req.cookies['admin'] == 'false') {
		res.clearCookie('flag3/4');
	} else if (req.cookies['admin'] === 'true') {
		res.cookie('flag3/4', '3b5ite_i');
	}
	res.render('index.html');
});

app.get('/hello', checkAdmin, function(req, res) {
	res.send('Hello, World!');
});

app.post('/login', checkAdmin, function(req, res) {
	res.cookie('user', req.body.username);
	res.redirect('/');
});

app.get('/findflag', checkAdmin, function(req, res) {
	res.render('click.html', { flag: 'Nope' });
});

app.post('/findflag', checkAdmin, function(req, res) {
	res.render('click.html', { flag: 'S_k00L!}' });
});

app.get('/*', checkAdmin, function(req, res) {
	var response = fs.readFileSync('templates/404.html');
	res.status(404).send(response.toString());
});

var server = app.listen(port, function() {});
console.log(`Server is listening on port ${port}`);
