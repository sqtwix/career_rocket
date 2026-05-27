% rebase('layout.tpl', title='Отзывы о продукте', year=year)

<div class="container">
    <div class="page-header">
        <h1>Отзывы наших клиентов</h1>
    </div>

    <div class="window">
        <h2>Оставить отзыв</h2>
        % if errors:
        <div class="alert alert-error">
            <ul style="margin: 0; padding-left: 20px;">
                % for err in errors:
                <li>{{!err}}</li>
                % end
            </ul>
        </div>
        % end
        <form action="/feedback" method="post">
            <div class="form-group">
                <label for="author">Ваше имя:</label>
                <input type="text" id="author" name="author" value="{{author}}" placeholder="Иван Петров" required>
            </div>
            <div class="form-group">
                <label for="email">Ваш email:</label>
                <input type="text" id="email" name="email" value="{{email}}" placeholder="example@mail.com" required>
            </div>
            <div class="form-group">
                <label for="text">Ваш отзыв:</label>
                <textarea id="text" name="text" rows="5" placeholder="Поделитесь впечатлениями..." required>{{text}}</textarea>
            </div>
            <button type="submit" class="btn-submit">Разместить</button>
        </form>
    </div>

    <div class="window">
        <h2>Что говорят клиенты</h2>
        % if not reviews:
        <p style="text-align: center; color: #888;">Пока нет отзывов. Станьте первым!</p>
        % else:
        <div class="reviews-list">
            % for rev in reviews:
            <div class="review-card">
                <div class="review-header">
                    <strong class="review-author">{{rev['author']}}</strong>
                    <span class="review-date">{{rev['date'][:10]}}</span>
                </div>
                <div class="review-text">
                    {{!rev['text'].replace('\n', '<br>')}}
                </div>
            </div>
            % end
        </div>
        % end
    </div>
</div>