/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: usrRect

    property string inputText: "input"
    property bool echoPwdMode: false
    width: 259
    height: 38
    border.color: "blue"
    TextInput {
        id: usrInput
        anchors.fill: parent
        verticalAlignment: TextInput.AlignVCenter
        horizontalAlignment: TextInput.AlignHCenter
        selectByMouse: true
        focus: true
        clip: true
        font.pixelSize: 18
        text: inputText
        echoMode: echoPwdMode?TextInput.Password:TextInput.Normal
    }
}

