<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title or 'Career Rocket'}}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: #0A1929;
            color: #FFFFFF;
            line-height: 1.5;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* Шапка */
        .navbar {
            background: rgba(10, 25, 41, 0.95);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-bottom: 2px solid rgba(171, 224, 240, 0.1);
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .nav-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #E2852E, #F5C857);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-menu {
            display: flex;
            gap: 32px;
            list-style: none;
        }

        .nav-menu a {
            color: #FFFFFF;
            text-decoration: none;
            font-weight: 500;
            padding: 8px 0;
            position: relative;
            transition: color 0.3s ease;
        }

        .nav-menu a::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #E2852E, #F5C857);
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.3s ease;
        }

        .nav-menu a:hover {
            color: #F5C857;
        }

        .nav-menu a:hover::before {
            transform: scaleX(1);
            transform-origin: left;
        }

        /* Контент */
        .content {
            max-width: 1280px;
            margin: 40px auto;
            padding: 0 24px;
            flex: 1;
            width: 100%;
        }

        /* Стили для страницы offers */
        .section-header {
            text-align: center;
            margin-bottom: 48px;
        }

        .section-header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #E2852E 0%, #F5C857 50%, #ABE0F0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
        }

        .section-header p {
            font-size: 1.125rem;
            color: #ABE0F0;
            max-width: 600px;
            margin: 0 auto;
        }

        .packages-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
            margin: 32px 0;
        }

        .package-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(20px);
            border: 2px solid rgba(171, 224, 240, 0.1);
            border-radius: 32px;
            padding: 32px 24px;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .package-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 30px 40px -15px rgba(226, 133, 46, 0.4);
            border-color: #E2852E;
        }

        .package-card.popular {
            background: linear-gradient(135deg, rgba(226, 133, 46, 0.15), rgba(245, 200, 87, 0.15));
            border-color: #E2852E;
        }

        .popular-badge {
            position: absolute;
            top: 20px;
            right: -10px;
            background: #E2852E;
            color: white;
            padding: 8px 30px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 8px 8px 8px 30px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            border-left: 3px solid #F5C857;
        }

        .package-header {
            margin-bottom: 24px;
            padding-bottom: 24px;
            border-bottom: 2px solid rgba(171, 224, 240, 0.2);
        }

        .badge {
            display: inline-block;
            background: rgba(171, 224, 240, 0.1);
            border: 1px solid #ABE0F0;
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 0.875rem;
            color: #ABE0F0;
            margin-bottom: 12px;
        }

        .package-name {
            font-size: 1.875rem;
            font-weight: 700;
            background: linear-gradient(135deg, #E2852E, #F5C857);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }

        .package-price {
            display: flex;
            align-items: baseline;
            gap: 8px;
            margin-top: 16px;
        }

        .price-amount {
            font-size: 2.5rem;
            font-weight: 800;
            color: #FFFFFF;
        }

        .price-period {
            font-size: 1rem;
            color: #ABE0F0;
        }

        .package-description {
            color: #ABE0F0;
            margin: 16px 0 24px;
            line-height: 1.6;
        }

        .features-list {
            list-style: none;
            margin: 0 0 32px;
            flex-grow: 1;
        }

        .feature-item {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            color: #FFFFFF;
        }

        .feature-icon.check {
            color: #F5C857;
            font-size: 18px;
        }

        .feature-icon.circle {
            color: #ABE0F0;
            opacity: 0.6;
            font-size: 18px;
        }

        .consultation-tag {
            background: rgba(245, 200, 87, 0.1);
            border: 1px solid #F5C857;
            color: #F5C857;
            font-size: 0.875rem;
            padding: 6px 12px;
            border-radius: 60px;
            display: inline-block;
            margin: 16px 0;
        }

        .btn {
            display: block;
            width: 100%;
            padding: 16px 24px;
            border-radius: 60px;
            font-weight: 600;
            font-size: 1.125rem;
            text-align: center;
            cursor: pointer;
            border: 2px solid #E2852E;
            background: transparent;
            color: #E2852E;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background: #E2852E;
            color: #0A1929;
        }

        .btn-primary {
            background: linear-gradient(135deg, #E2852E, #F5C857);
            border: none;
            color: #0A1929;
        }

        .btn-primary:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(226, 133, 46, 0.5);
        }

        /* Футер */
        footer {
            background: rgba(10, 25, 41, 0.95);
            border-top: 2px solid rgba(171, 224, 240, 0.1);
            padding: 30px 0;
            text-align: center;
            color: #ABE0F0;
            margin-top: 40px;
        }

        .footer-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 24px;
        }

        @media (max-width: 768px) {
            .nav-container {
                flex-direction: column;
                gap: 15px;
            }
            
            .nav-menu {
                gap: 20px;
            }
            
            .section-header h1 {
                font-size: 2rem;
            }
        }
    </style>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Career Rocket</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/mainpage.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">Career Rocket</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/home">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/analytics">Analytic</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Career Rocket</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>