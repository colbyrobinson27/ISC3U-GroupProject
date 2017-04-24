def openFile(fileName,scene):
    file1 = open("./Levels/" + fileName,"r")
    data = file1.read()
    data = data[:len(data)-1].split("/")
    scenery = data[1][:len(data[1])].split(",")
    print(scenery)
    data = data[0][:len(data[0])-1].split("-")
    tiles = data[1].split(",")
    size = data[0].split(",")
    size[0] = int(size[0])
    size[1] = int(size[1])
    print(size,tiles)
    map = []
    tileSet = ['caveWall', 'caveFloor', 'grass1', 'desert1']
    scenerySet = ['tree1','stag1','cactus1']
    for i in range(int(size[1])):
        map.append([])
    y = 0
    for i in range(int(size[1])-1,-1,-1):

        for g in range(int(size[0])):
            for h in range(len(tileSet)):

                if tiles[y*int(size[0]) + g] == tileSet[h]:
                    map[i].append(h)
        y+=1
    y = 0
    for i in range(int(size[1])):
        scene.append([])
        for g in range(int(size[0])):
            scene[i].append(0)
    for i in range(int(size[1])-1,-1,-1):
        for g in range(int(size[0])):
            for h in range(len(scenerySet)):
                if scenery[y*int(size[0])+g] == scenerySet[h]:
                    scene[i][g] = h+1

        y+=1

    return map
