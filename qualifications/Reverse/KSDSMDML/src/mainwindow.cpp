#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->toolButton, &QToolButton::pressed,
            this, [this]() {
        incrementValue(ui->lineEdit);
    });

    connect(ui->toolButton_2, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit);
    });

    connect(ui->toolButton_3, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_2);
    });

    connect(ui->toolButton_4, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_2);
    });

    connect(ui->toolButton_5, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_3);
            });

    connect(ui->toolButton_6, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_3);
            });

    connect(ui->toolButton_7, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_4);
            });

    connect(ui->toolButton_8, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_4);
            });

    connect(ui->toolButton_9, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_5);
            });

    connect(ui->toolButton_10, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_5);
            });

    connect(ui->toolButton_11, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_6);
            });

    connect(ui->toolButton_12, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_6);
            });

    connect(ui->toolButton_13, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_7);
            });

    connect(ui->toolButton_14, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_7);
            });

    connect(ui->toolButton_15, &QToolButton::pressed,
            this, [this]() {
                incrementValue(ui->lineEdit_8);
            });

    connect(ui->toolButton_16, &QToolButton::pressed,
            this, [this]() {
                decrementValue(ui->lineEdit_8);
            });
}

void MainWindow::incrementValue(QLineEdit *lineEdit) {
    ushort val = lineEdit->text().toUShort(nullptr, 16);
    val = (val + 1) % 0x10;
    lineEdit->setText(QString::number(val, 16).toUpper());
}

void MainWindow::decrementValue(QLineEdit *lineEdit) {
    ushort val = lineEdit->text().toUShort(nullptr, 16);
    val = (val - 1) % 0x10;
    lineEdit->setText(QString::number(val, 16).toUpper());
}
