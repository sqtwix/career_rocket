% rebase('layout.tpl', title='Отзывы о продукте', year=year)

<container class="container">
    <header class="page-header">
        <h1>Отзывы наших клиентов</h1>
    </header>

    <section class="window">
        <h2>Оставить отзыв</h2>
        % if errors:
        <div class="alert alert-error">
            <ul>
                % for err in errors:
                <li>{{!err}}</li>
                % end
            </ul>
        </div>
        % end
        <form action="/feedback" method="post">
            <fieldset>
                <div class="form-group">
                    <label for="author">Ваше имя:</label>
                    <input type="text" id="author" name="author" value="{{author}}" placeholder="Иван Петров" required>
                </div>
                <div class="form-group">
                    <label for="email">Ваш email:</label>
                    <input type="email" id="email" name="email" value="{{email}}" placeholder="example@mail.com" required>
                </div>
                <div class="form-group">
                    <label for="title">Заголовок отзыва:</label>
                    <input type="text" id="title" name="title" value="{{title}}" placeholder="Коротко о сути" required>
                </div>
                <div class="form-group">
                    <label for="text">Ваш отзыв:</label>
                    <textarea id="text" name="text" rows="5" placeholder="Поделитесь впечатлениями..." required>{{text}}</textarea>
                </div>
                <button type="submit" class="btn-submit">Разместить</button>
            </fieldset>
        </form>
    </section>

    <section class="window">
        <h2>Что говорят клиенты</h2>
        % if not reviews:
        <p style="text-align: center; color: #888;">Пока нет отзывов. Станьте первым!</p>
        % else:
        <div class="reviews-list">
            % for rev in reviews:
            <article class="review-card">
                <div class="review-header">
                    <strong class="review-author">{{rev['author']}}</strong>
                    <time class="review-date" datetime="{{rev['date']}}">{{rev['date'][:10]}}</time>
                </div>
                % if rev.get('email'):
                <address class="review-email">{{rev['email']}}</address>
                % end
                % if rev.get('title'):
                <h3 class="review-title">{{rev['title']}}</h3>
                % end
                <p class="review-text">
                    {{!rev['text'].replace('\n', '<br>')}}
                </p>
            </article>
            % end
        </div>
        % end
    </section>
</container>