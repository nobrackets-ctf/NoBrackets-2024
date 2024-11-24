#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLineEdit>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);

private slots:
    void incrementValue(QLineEdit *lineEdit);
    void decrementValue(QLineEdit *lineEdit);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
