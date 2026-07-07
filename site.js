selectTab = function () {
    let currentTab = document.querySelector('[aria-selected=true]');
    currentTab.setAttribute('aria-selected', 'false')
    currentTab.classList.remove('contrast')
    let newTab = event.target
    newTab.setAttribute('aria-selected', 'true')
    newTab.classList.add('contrast')
}