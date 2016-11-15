TEMPLATE = app
DEPENDPATH += .
INCLUDEPATH += . .. ../..

# enable/disable debug symbols
#CONFIG += debug
CONFIG += release

debug {
  OBJECTS_DIR = obj/debug
  QMAKE_LIBDIR += ../../lib/debug ../../quackleio/lib/debug
}

release {
  OBJECTS_DIR = obj/release
  QMAKE_LIBDIR += ../../lib/release ../../quackleio/lib/release
}

win32:!win32-g++ {
  LIBS += -lquackleio -llibquackle
} else {
  LIBS += -lquackleio -lquackle
}


# Input
HEADERS += trademarkedboards.h
SOURCES += iotest.cpp trademarkedboards.cpp

macx-g++ {
    QMAKE_CXXFLAGS += -fpermissive
}
