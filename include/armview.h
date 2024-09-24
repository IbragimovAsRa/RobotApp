#ifndef ARMVIEW_H
#define ARMVIEW_H

#include "armmodel.h"

class ArmView {

    ArmView() {

    }

    void setModel(ArmModel* armModel) {
        _armModel = armModel;
    }

private:
    ArmModel* _armModel = nullptr;
};

#endif // ARMVIEW_H
