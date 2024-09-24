#ifndef ARMMODEL_H
#define ARMMODEL_H

#include <QPointF>
#include <QHash>
#include <QVector>

class ArmModel
{
    ArmModel() {

    }

    void addPoint(int id, QPointF pos);
    QPointF point(int id);

    QVector<QPointF> _configure;


};

#endif // ARMMODEL_H
