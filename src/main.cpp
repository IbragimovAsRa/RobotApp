#include <Python.h>
#include <boost/python.hpp>
#include <wchar.h>
#include <iostream>
#include <QDebug>
#include <QString>
#include <QFile>
#include <QApplication>
#include <cstdlib>   // для функции system

using namespace boost::python;

int main(int argc, char *argv[]) {
//    QApplication app(argc, argv);

    try {
        // Инициализация Python
        Py_Initialize();

        // Импорт корневого модуля
        object main_m = import("__main__");
        object main_ns= main_m.attr("__dict__");

        QFile file(":/armdetector.py");
        file.open(QIODevice::ReadOnly | QIODevice::Text);

        // Загрузка скрипта Python
        exec(file.readAll(), main_ns);

        // Получаем функцию
        object detect_arm = main_ns["detect_arm"];
        object p_arm =  detect_arm();

        list configure = extract<list>(p_arm);




        for (int i = 0; i < 21; i++ ) {
//            qDebug() << "\n" << extract<double>(configure[i]);
        }

    } catch (const boost::python::error_already_set&) {
        PyErr_Print(); // Печать ошибок Python
    }
    Py_Finalize();
//    return app.exec();
    return 0;
}

