/**
 * Change selected tab in navbar.
 */
selectTab = function () {
    // Change current tab to secondary button style
    let currentTab = document.querySelector('[aria-selected=true]');
    currentTab.setAttribute('aria-selected', 'false');
    currentTab.classList.add('secondary');

    // Change new tab to primary button style
    let newTab = event.target;
    newTab.setAttribute('aria-selected', 'true');
    newTab.classList.remove('secondary');
    newTab.blur();
}