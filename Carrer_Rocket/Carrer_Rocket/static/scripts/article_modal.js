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