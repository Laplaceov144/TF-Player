document.getElementById('fill-btn').addEventListener('click', (e) => {
    e.preventDefault();
    [...document.querySelectorAll('ol li')].forEach(item => {
        item.querySelector('input').value = item.querySelector('.item-text').innerText;
    });
});
