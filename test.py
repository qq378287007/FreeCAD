import FreeCAD
doc = FreeCAD.newDocument("Unnamed")

cylinder = doc.addObject("Part::Cylinder", "Cylinder")
box = doc.addObject("Part::Box", "box")

vec1 = FreeCAD.Vector(2, 0, 0)
vec2 = FreeCAD.Vector(0, 3, 0)
vec3 = vec1.add(vec2)

box.Placement.Base = vec3
placement = FreeCAD.Placement()
box.Placement = placement

#Object
vo = box.ViewObject
vo.Transparency = 80
vo.hide()
vo.show()

doc.supportedTypes()

doc.recompute()




import Mesh
Mesh.export(obj, "test.obj")

