export function settingsMenu() {
    document.querySelector('main').innerHTML = '<div class="page-content settings">\n' +
        '        <input type="checkbox" id="settings__sound" checked>\n' +
        '        <label for="settings__sound">\n' +
        '          <p>Sound</p>\n' +
        '          <img class="settings__sound__icon" src="static/assets/icons/sound.svg">\n' +
        '        </label>\n' +
        '    \n' +
        '        <input type="checkbox" id="settings__animations" checked>\n' +
        '        <label for="settings__animations">\n' +
        '          <p>3D Animations</p>\n' +
        '          <img class="settings__animations__icon" src="static/assets/icons/animations.svg">\n' +
        '        </label>\n' +
        '    </div>';
}
