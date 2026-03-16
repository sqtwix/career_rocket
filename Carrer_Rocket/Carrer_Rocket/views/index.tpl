<link rel="stylesheet" href="/static/content/mainpage.css">

<div class="jumbotron">
    <img src="static/images/rocket.png" width="200" height="150">
    <p class="lead">Career Rocket помогает находить работу и стажировку в сфере IT.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<dif class="search">
    <form action="/search" metod="get" class="search-form">
    <div class="search-input-group">
        <input type="text" name="query" placeholder="Поиск вакансий, стажировок..." class="search-input">
        <button type="subtim" class="btn btn-default">Найти</button>
    </div>
    </form>
<div class="popular-tags">
        <a href="/search?query=python" class="tag">Python</a>
        <a href="/search?query=javascript" class="tag">JavaScript</a>
        <a href="/search?query=стажировка" class="tag">Стажировка</a>
        <a href="/search?query=frontend" class="tag">Frontend</a>
    </div>
</div>

<div class="row">
    <div class="container">
        <div class="col-md-4">
            <h2>Getting started</h2>
            <p>
                Bottle gives you a powerful, patterns-based way to build dynamic websites that
                enables a clean separation of concerns and gives you full control over markup
                for enjoyable, agile development.
            </p>
            <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Learn more &raquo;</a></p>
        </div>
        <div class="col-md-4">
            <h2>Get more libraries</h2>
            <p>The Python Package Index is a repository of software for the Python programming language.</p>
            <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
        </div>
        <div class="col-md-4">
            <h2>Microsoft Azure</h2>
            <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
            <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
        </div>
    </div>
</dif>
