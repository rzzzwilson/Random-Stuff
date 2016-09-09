var menu = document.querySelector('.menu');

function showMenu(x, y)
{
    menu.style.left = x + 'px';
    menu.style.top = y + 'px';
    menu.classList.add('show-menu');
}

function hideMenu()
{
    menu.classList.remove('show-menu');
}

function onContextMenu(e)
{
    e.preventDefault();
    showMenu(e.pageX, e.pageY);
    document.addEventListener('click', onClick, false);
}

function onClick(e)
{
    hideMenu();
    document.removeEventListener('click', onClick);
}

document.addEventListener('contextmenu', onContextMenu, false);
