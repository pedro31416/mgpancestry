data <- jsonlite::fromJSON("output.JSON")

library(igraph)
ancestry_adj_mat <- sapply(data$children, function(x) is.element(data$id, x))
ancestry_graph <- graph_from_adjacency_matrix(ancestry_adj_mat)
V(ancestry_graph)$name <- data$name

g2 <- make_ego_graph(ancestry_graph, 18, 1)[[1]]
my_layout = norm_coords(layout.reingold.tilford(g2, flip.y = FALSE, circular = FALSE))
my_layout[,1] <- my_layout[,1]*1.6
my_layout[,2] <- my_layout[,2]*1.1
plot(g2, 
     layout = my_layout,
     vertex.shape = "none",
     vertex.label.cex = 0.5,
     vertex.label.degree = pi/2,
     edge.arrow.size = 0.2,
     edge.arrow.mode = "-",
     edge.width = 1.5,
     rescale = FALSE)

# plot(g, layout = layout.reingold.tilford(g, flip.y = FALSE, circular = FALSE), 
#      vertex.shape = "crectangle",
#      vertex.color = "lightblue",
#      vertex.size = 20,
#      vertex.size2 = 2,
#      vertex.label.cex = 0.2,
#      vertex.label.degree = pi/2,
#      edge.arrow.size = 0.2, 
#      edge.arrow.mode = "<-")
