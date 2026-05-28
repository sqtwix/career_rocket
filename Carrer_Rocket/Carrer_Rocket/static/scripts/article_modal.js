function openModal(title, author, postDate, text) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalAuthor').textContent = author;
    document.getElementById('modalDate').textContent = postDate;
    document.getElementById('modalText').innerHTML = text.replace(/\n/g, '<br>');
    document.getElementById('articleModal').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('articleModal').style.display = 'none';
    document.body.style.overflow = 'auto';
}

window.onclick = function(event) {
    const modal = document.getElementById('articleModal');
    if (event.target === modal) {
        closeModal();
    }
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

function scrollToArticle(articleId) {
    setTimeout(function() {
        const element = document.getElementById(articleId);
        if (element) {
            const offset = 80;
            const elementPosition = element.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
            
            element.style.transition = 'all 0.3s ease';
            element.style.borderColor = '#E2852E';
            element.style.boxShadow = '0 0 20px rgba(226, 133, 46, 0.5)';
            
            setTimeout(function() {
                element.style.borderColor = '';
                element.style.boxShadow = '';
            }, 2000);
        }
    }, 300);
}

function scrollToArticlesList() {
    setTimeout(function() {
        const articlesList = document.querySelector('.articles-list');
        if (articlesList) {
            const offset = 80;
            const elementPosition = articlesList.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
            
            articlesList.style.transition = 'all 0.3s ease';
            articlesList.style.backgroundColor = 'rgba(226, 133, 46, 0.1)';
            
            setTimeout(function() {
                articlesList.style.backgroundColor = '';
            }, 1000);
        }
    }, 300);
}