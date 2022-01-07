import xml.etree.ElementTree as ET

classes = ["包","女"]

def convert(box):

    x = box[0]
    w = box[1]
    y = box[2]
    h = box[3]
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('E:\\Users\\lenovo\\Desktop\\labelimg\\%s.xml' % (image_id),encoding='utf-8')

    out_file = open('E:\\Users\\lenovo\\Desktop\\labelimg\\%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert( b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


image_ids_train = open('E:\\Users\\lenovo\\Desktop\\33.txt').read().strip().split()

for image_id in image_ids_train:
    convert_annotation(image_id)