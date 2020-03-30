import networkx as nx
import matplotlib.pyplot as plt

#create a graph with all characters
GoT=nx.Graph() 
# adding 20 characters 
GoT.add_nodes_from(['Daenerys','Howland','AerysII','Jaime','Viserys', 
'Lyanna','Elia','Arthur','JonArryn','RhaenysNAegon','Rhaegar','Gregor', 
'Rhaella','Rickard','Robert','JonSnow','Benjen','Ned','Brandon',
'Tywin']) 
#---------------------------------------------------------------------------   
 
#---------------------------------------------------------------------------   
# abduction links  - we create another graph for it - but it has to be directed because abduction is a directionalc relationship 
Abduct=nx.DiGraph() 
#adding the links - there's only 1 instance of it 
Abduct.add_edges_from([('Rhaegar','Lyanna')],label='abducted')
#extracting labels from the list of edges   
Abduct_labels=nx.get_edge_attributes(Abduct,'label') 
#--------------------------------------------------------------------------   
 
#---------------------------------------------------------------------------   
# served links - - we create another graph for serve links - it has to be directed because Serve is a directional relationship 
Serve=nx.DiGraph() 
#adding the links - here are 3 instances of it   
Serve.add_edges_from([('Arthur','AerysII'),('Gregor','Tywin'),('Jaime','AerysII')
],label='served')
#extracting labels from the list of edges 
Serve_labels=nx.get_edge_attributes(Serve,'label') 
#---------------------------------------------------------------------------   

#---------------------------------------------------------------------------   
# Guardian links - - we create another graph for serve links - it has to be directed because Guardian is a directional relationship 
Guardian=nx.DiGraph() 
#Guardian the links - there are 3 instances of it   
Guardian.add_edges_from([('Ned','JonSnow'),('JonArryn','Robert'),('JonArryn','Ned')],label='guardian') 
#extracting labels from the list of edges   
Guardian_labels=nx.get_edge_attributes(Guardian,'label') 
#---------------------------------------------------------------------------   
 
#---------------------------------------------------------------------------   
#Kill links - we create another graph for serve links - it has to be directed because Kill is a directional relationship   
Kill=nx.DiGraph() 
#Guardian the links - there are 8 instances of it   
Kill.add_edges_from([('Ned','Arthur'),('Gregor','RhaenysNAegon'),('Gregor','Elia'),('Howland','Arthur'),('AerysII','Brandon'),('AerysII','Rickard'),('Jaime','AerysII'),('Robert','Rhaegar')],label='killed')
#extracting labels from the list of edges   
Kill_labels=nx.get_edge_attributes(Kill,'label')
#---------------------------------------------------------------------------   
 
#---------------------------------------------------------------------------  
Married=nx.Graph()
Married.add_edges_from([('Rhaegar','Elia'),('Robert','Lyanna'),('AerysII','Rhaella')],label='married')
Married_labels=nx.get_edge_attributes(Married,'label')

Allies=nx.Graph()
Allies.add_edges_from([('Tywin','Robert'),('Robert','JonArryn'),('Robert','Ned'),('Ned','Howland')],label='allies')
Allies_labels=nx.get_edge_attributes(Allies,'label')

Parent=nx.DiGraph()
Parent.add_edges_from([('Elia','RhaenysNAegon'),('Rhaegar','RhaenysNAegon'),('Rickard','Ned'),('Rhaella','Viserys'),('Rhaella','Rhaegar'),('Rhaella','Daenerys'),('Rickard','Lyanna'),('Rickard','Benjen'),('Lyanna','JonSnow'),('Rhaegar','JonSnow'),('AerysII','Rhaegar'),('Tywin','Jaime'),('AerysII','Daenerys'),('AerysII','Viserys')],label='parent')
Parent_labels=nx.get_edge_attributes(Parent,'label')

Sibling=nx.Graph()
Sibling.add_edges_from([('Lyanna','Ned'),('Lyanna','Benjen'),('Lyanna','Brandon'),('Ned','Brandon'),('Ned','Benjen'),('Rhaella','AerysII'),('Benjen','Brandon'),('Rhaegar','Viserys'),('Rhaegar','Daenerys'),('Daenerys','Viserys')],label='sibling')
Sibling_labels=nx.get_edge_attributes(Sibling,'label')
#redrawing nodes and Abduct links   
plt.figure(1,figsize=(12,12)) 
pos=nx.circular_layout(GoT) 
nx.draw(GoT,pos,node_color='grey',node_size=5,with_labels=True) 
nx.draw_networkx_edges(Abduct,pos,edge_color='deeppink') 
nx.draw_networkx_edge_labels(Abduct,pos,edge_labels=Abduct_labels,label_pos=0.2, 
font_color='deeppink') 
#overlaying Serve links on GoT and Abduct links   
#drawing the purple Serve edges   
nx.draw_networkx_edges(Serve,pos,edge_color='purple') 
#adding purple Serve labels to the grarph   
nx.draw_networkx_edge_labels(Serve,pos,edge_labels=Serve_labels,label_pos=0.2,
font_color='purple')
#overlaying Guardian links on GoT and Abduct+Serve links   
#drawing the blue Guardian edges   
nx.draw_networkx_edges(Guardian,pos,edge_color='blue')
#adding blue Guardian labels to the grarph   
nx.draw_networkx_edge_labels(Guardian,pos,edge_labels=Guardian_labels,label_pos=0.2,
font_color='blue')
#overlaying Kill links on GoT and Abduct+Serve+Guardian links   
#drawing green Kill edges   
nx.draw_networkx_edges(Kill,pos,edge_color='green')
#extracting labels from the list of edges   
Kill_labels=nx.get_edge_attributes(Kill,'label')
#adding green Kill labels to the grarph   
nx.draw_networkx_edge_labels(Kill,pos,edge_labels=Kill_labels,label_pos=0.2, 
font_color='green')

nx.draw_networkx_edges(Married,pos,edge_color='orange')
nx.draw_networkx_edge_labels(Married,pos,edge_labels=Married_labels,label_pos=0.2,
font_color='orange')

nx.draw_networkx_edges(Allies,pos,edge_color='cyan')
nx.draw_networkx_edge_labels(Allies,pos,edge_labels=Allies_labels,label_pos=0.2,
font_color='cyan')

nx.draw_networkx_edges(Parent,pos,edge_color='black')
nx.draw_networkx_edge_labels(Parent,pos,edge_labels=Parent_labels,label_pos=0.2,
font_color='black')

nx.draw_networkx_edges(Sibling,pos,edge_color='skyblue')
nx.draw_networkx_edge_labels(Sibling,pos,edge_labels=Sibling_labels,label_pos=0.2,
linestyle='--',font_color='skyblue')

plt.show() 
#-------------------------------------------------------------------
#showing a list of directed relationships a character is involved in   
for n in GoT.nodes():
        print(n,':',Abduct.degree(n),Serve.degree(n),Guardian.degree(n),Kill.out_degree(n))