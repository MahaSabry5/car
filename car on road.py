from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,100)
    gluLookAt(8,9,10,0,0,0,0,1,0)
    
angle=0
x=0
increasing=1
    
def draw():
    global angle
    global x
    global increasing
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.2,0.4,0.2,1)
    
    glLoadIdentity()#road
    glColor3f(0.6,0.6,0.6)
    glTranslate(0,0,0)
    glScale(10,0,0.75)
    glutSolidCube(8)

    glLoadIdentity()#roadline1
    glColor3f(1,1,1)
    glTranslate(7,0,0)
    glScale(2,0,0.5)
    glutSolidCube(2)
    
    glLoadIdentity()#roadline2
    glColor3f(1,1,1)
    glTranslate(1,0,0)
    glScale(2,0,0.5)
    glutSolidCube(2)
    
    glLoadIdentity()#roadline3
    glColor3f(1,1,1)
    glTranslate(-6,0,0)
    glScale(2.5,0,0.5)
    glutSolidCube(2)

    glLoadIdentity()#roadline4
    glColor3f(1,1,1)
    glTranslate(-15,0,0)
    glScale(2.5,0,0.5)
    glutSolidCube(2)

    glLoadIdentity()#tree1
    glColor3f(0.3,0.1,0.1)
    glTranslate(3,0,-10)
    glScale(0.4,3,-0.5)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(0.3,0.7,0.1)
    glTranslate(3,2,-10)
    glutSolidSphere(2,10,10)
    glColor3f(0.3,0.4,0.3)
    glutWireSphere(2,10,10)

    
    glLoadIdentity()#tree2
    glColor3f(0.3,0.1,0.1)
    glTranslate(-7,0,-10)
    glScale(0.4,3,-0.5)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(0.3,0.7,0.1)
    glTranslate(-7,2,-10)
    glutSolidSphere(2,10,10)
    glColor3f(0.3,0.4,0.3)
    glutWireSphere(2,10,10)
    
    glLoadIdentity()#tree3
    glColor3f(0.3,0.1,0.1)
    glTranslate(-22,0,-10)
    glScale(0.4,3,-0.5)
    glutSolidCube(2)
    glLoadIdentity()
    glColor3f(0.3,0.7,0.1)
    glTranslate(-22,2,-10)
    glutSolidSphere(2,10,10)
    glColor3f(0.3,0.4,0.3)
    glutWireSphere(2,10,10)
    
    glLoadIdentity()#body
    glColor3f(0.5,0,0.5)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)
    glColor3f(0,0,0)
    glutWireCube(5)
    
    glLoadIdentity()#body1
    glColor3f(0.5,0,0.5)
    glTranslate(x+0,1.25,0)
    glScale(0.5,0.25,0.5)
    glutSolidSphere(3.5,10,10)
    glColor3f(0,0,0)
    glutWireSphere(3.5,10,10)


    glLoadIdentity()#wheel1
    glColor3f(0,0,0)
    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.25,0.5,12,8)

    glLoadIdentity()#wheel2
    glTranslate(x+2.5,-2.5*0.25,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(.25,0.5,12,8)

    glLoadIdentity()#wheel3
    glTranslate(x+-2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutSolidTorus(0.25,0.5,12,8)

    #glLoadIdentity()#wheel4
    #glTranslate(x+-2.5,-2.5*0.25,-2.5*0.5)
    #glRotate(angle,0,0,1)
    #glutSolidTorus(0.25,0.5,12,8)
    
    glLoadIdentity()#light1
    glColor3f(1,1,0)
    glTranslate(x+2.5,0.5,-1)
    glutWireSphere(0.3,10,10)

    glLoadIdentity()#light2
    glColor3f(1,1,0)
    glTranslate(x+2.5,0.5,1.3)
    glutWireSphere(0.3,10,10)

    if increasing:
            angle-=0.1
            x+=0.005
            if x >5:
              increasing=0
    else:
            angle+=0.1
            x-=0.005
            if x <-15:
                increasing=1
        
    glutSwapBuffers()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"TEAPOT")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()
