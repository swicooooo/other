import QtQuick 2.15
import QtQuick.Controls 2.15
import QmlDemo
import QtQuick.Layouts

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: Constants.backgroundColor

    Image {
        id: backImg
        source: "images/back.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    ColumnLayout {
        id: columnLayout
        anchors.centerIn: parent
        spacing: 20

        ColumnLayout {
            x: 208
            y: 182
            spacing: 10
            EntryInput {
                id: usrRect
                inputText: qsTr("admin")
            }
            EntryInput {
                id: pwdRect
                inputText: qsTr("admin")
                echoPwdMode: true
            }
        }

        RowLayout {
            spacing: 60
            EntryField {
                id: signIn
                buttonText: qsTr("Sign in")
            }
            EntryField {
                id: signUp
                buttonText: qsTr("Sign up")
            }
        }
    }
}

