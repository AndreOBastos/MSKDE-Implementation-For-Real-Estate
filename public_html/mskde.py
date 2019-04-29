class Coordinates:
	def __init__(self,lat,lon):
		self.lat = lat
		self.lon = lon

class Vertex:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Edge:
	def __init__(self, left_top_vertex, right_bottom_vertex):
		self.left_top_vertex = left_top_vertex
		self.right_bottom_vertex = right_bottom_vertex

def lookup(top_left, top_right, bottom_left, bottom_right, value):
	if(top_left>value):
		if(top_right>value):
			if(bottom_left>value):
				if(bottom_right>value): #1111
					return 0
				else: #1110
					return 2
			else: 
				if(bottom_right>value): #1101
					return 1
				else: #1100
					return 3
		else:
			if(bottom_left>value):
				if(bottom_right>value): #1011
					return 4
				else: #1010
					return 6
			else:
				if(bottom_right>value): #1001
					return 5
				else: #1000
					return 7
	else:
		if(top_right>value):
			if(bottom_left>value):
				if(bottom_right>value): #0111
					return 8
				else: #0110
					return 10
			else:
				if(bottom_right>value): #0101
					return 9
				else: #0100
					return 11
		else:
			if(bottom_left>value):
				if(bottom_right>value): #0011
					return 12
				else: #0010
					return 14
			else:
				if(bottom_right>value): #0001
					return 13
				else: #0000
					return 15

def interpolate(value1, value2, cell_size): #value1 > value2
	total = value1+value2
	if(value1 > value2)
		return (value2/total) * cell_size;
	else:
		return (value1/total) * cell_size;


def MSKDE_value(value, KDE_Matrix, Coord_Matrix, square_size):
	Edge_Array = []
	for y in range(len(KDE_Matrix)):
		for x in range(len(KDE_Matrix[y])):
			MS_type = lookup(KDE_Matrix[x][y],KDE_Matrix[x+1][y],KDE_Matrix[x][y+1],KDE_Matrix[x+1][y+1], value)
			longitude = Coord_Matrix[x][y]
			if(MS_type==1):
				interp1 = interpolate(Coord_Matrix[x][y], Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude + interp1)
				interp2 = interpolate(Coord_Matrix[x][y+1], Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + interp2, latitude+cell_size)
				e = Edge(v2,v1)
				Edge_Array.append(e)

			elif(MS_type==2):
				interp1 = interpolate(Coord_Matrix[x][y+1],Coord_Matrix[x+1][y+1], square_size)
				v1 = Vertex(longitude+interp1, latitude+square_size)
				interp1 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude+square_size, latitude+interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==3):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude+interp1)
				interp2 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + square_size, latitude+interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==4):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v1 = Vertex(longitude + interp1, latitude)
				interp2 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + square_size, latitude + interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==5):
				v1 = Vertex(Coord_Matrix[x][y].lon - half_square, Coord_Matrix[x][y].lat)
				v2 = Vertex(Coord_Matrix[x][y].lon, Coord_Matrix[x][y].lat + half_square)
				v3 = Vertex(Coord_Matrix[x][y].lon + half_square, Coord_Matrix[x][y].lat)
				v4 = Vertex(Coord_Matrix[x][y].lon, Coord_Matrix[x][y].lat - half_square)
				if((Coord_Matrix[x][y] + Coord_Matrix[x+1][y] + Coord_Matrix[x][y+1] + Coord_Matrix[x+1][y+1])/4 < value):
					e1 = Edge(v1,v2)
					e2 = Edge(v4,v3)
					Edge_Array.append(e1)
					Edge_Array.append(e2)
				else:
					e1 = Edge(v1,v4)
					e2 = Edge(v2,v3)
					Edge_Array.append(e1)
					Edge_Array.append(e2)

			elif(MS_type==6):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v1 = Vertex(longitude + interp1, latitude)
				interp1 = interpolate(Coord_Matrix[x][y+1],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + interp2, latitude + square_size)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==7):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude+interp1)
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v2 = Vertex(longitude+interp2, latitude)
				e = Edge(v2,v1)
				Edge_Array.append(e)

			elif(MS_type==8):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude+interp1)
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v2 = Vertex(longitude+interp2, latitude)
				e = Edge(v2,v1)
				Edge_Array.append(e)

			elif(MS_type==9):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v1 = Vertex(longitude + interp1, latitude)
				interp1 = interpolate(Coord_Matrix[x][y+1],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + interp2, latitude + square_size)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==10):
				v1 = Vertex(Coord_Matrix[x][y].lon - half_square, Coord_Matrix[x][y].lat)
				v2 = Vertex(Coord_Matrix[x][y].lon, Coord_Matrix[x][y].lat + half_square)
				v3 = Vertex(Coord_Matrix[x][y].lon + half_square, Coord_Matrix[x][y].lat)
				v4 = Vertex(Coord_Matrix[x][y].lon, Coord_Matrix[x][y].lat - half_square)
				if((Coord_Matrix[x][y] + Coord_Matrix[x+1][y] + Coord_Matrix[x][y+1] + Coord_Matrix[x+1][y+1])/4 < value):
					e1 = Edge(v1,v4)
					e2 = Edge(v2,v3)
					Edge_Array.append(e1)
					Edge_Array.append(e2)
				else:
					e1 = Edge(v1,v2)
					e2 = Edge(v4,v3)
					Edge_Array.append(e1)
					Edge_Array.append(e2)

			elif(MS_type==11):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x+1][y], square_size)
				v1 = Vertex(longitude + interp1, latitude)
				interp2 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + square_size, latitude + interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==12):
				interp1 = interpolate(Coord_Matrix[x][y],Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude+interp1)
				interp2 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude + square_size, latitude+interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==13):
				interp1 = interpolate(Coord_Matrix[x][y+1],Coord_Matrix[x+1][y+1], square_size)
				v1 = Vertex(longitude+interp1, latitude+square_size)
				interp1 = interpolate(Coord_Matrix[x+1][y],Coord_Matrix[x+1][y+1], square_size)
				v2 = Vertex(longitude+square_size, latitude+interp2)
				e = Edge(v1,v2)
				Edge_Array.append(e)

			elif(MS_type==14):
				interp1 = interpolate(Coord_Matrix[x][y], Coord_Matrix[x][y+1], square_size)
				v1 = Vertex(longitude, latitude + interp1)
				interp2 = interpolate(Coord_Matrix[x+1][y+1], Coord_Matrix[x][y+1], square_size)
				v2 = Vertex(longitude + interp2, latitude+cell_size)
				e = Edge(v2,v1)
				Edge_Array.append(e)

