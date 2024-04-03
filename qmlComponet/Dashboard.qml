

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts

Item {
    id: root
    width: 800
    height: 560

    RowLayout {
        spacing: 0
        anchors.fill: parent
        ListView {
            id: personListView
            width: parent.width / 6
            height: parent.height
            model: ListModel {
                ListElement {
                    name: "Grey"
                    colorCode: "grey"
                }

                ListElement {
                    name: "Red"
                    colorCode: "red"
                }
            }
            delegate: Item {
                x: 5
                width: 80
                height: 40
                Row {
                    id: row1
                    spacing: 10
                    Rectangle {
                        width: 40
                        height: 40
                        color: colorCode
                    }

                    Text {
                        text: name
                        anchors.verticalCenter: parent.verticalCenter
                        font.bold: true
                    }
                }
            }
        }

        Rectangle {
            width: 1
            height: parent.height
            color: "black"
        }

        ListView {
            id: historyListView
            width: parent.width - personListView.width
            height: parent.height
            model: ListModel {
                ListElement {
                    name: "Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey Grey "
                    colorCode: "grey"
                    isMine: false
                }

                ListElement {
                    name: "Red Red Red Red Red Red Red Red Red"
                    colorCode: "red"
                    isMine: true
                }
            }
            delegate: Item {
                x: 5
                width: 80
                height: txt.height
                Row {
                    id: msgRow
                    spacing: 10
                    Rectangle {
                        id: r
                        width: 40
                        height: 40
                        color: colorCode
                    }
                    // 在本例ListView的parent是窗口
                    Text {
                        id: txt
                        width: historyListView.width-10-r.width-5
                        height: contentHeight
                        text: name
                        anchors.verticalCenter: parent.verticalCenter
                        font.bold: true
                        wrapMode: Text.WordWrap // 按照单词折叠
                    }
                }
            }
        }
    }

    Rectangle {
        id: toolRect
        width: historyListView.width
        height: 24
        anchors.right: parent.right
        anchors.bottom: inputRect.top
        border.color: "black"
        color: "transparent"

        Button {
            id: fileBt
            width: parent.width / 10
            height: 24

            Image {
                id: name
                anchors.fill: parent
                source: "images/back.png"
            }
            Text {
                text: "file"
                font.pixelSize: 18
                anchors.centerIn: parent
            }
        }
    }

    Rectangle {
        id: inputRect
        width: historyListView.width
        height: 74
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        border.color: "black"

        ScrollView {
            anchors.fill: parent
            TextArea {
                id: textArea
                focus: true
                wrapMode: TextArea.WordWrap
                selectByMouse: true
                font.pixelSize: 17
                anchors.fill: inputRect
                placeholderText: qsTr("Text Area")
            }
        }
    }
}

