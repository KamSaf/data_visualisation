const graph = new graphology.Graph();
graph.addNode("a", {
  x: 0,
  y: 0,
  label: "Kliknij mnie",
  size: 10,
  color: "#f00",
});
const renderer = new Sigma(graph, document.getElementById("container"));
renderer.on("clickNode", ({ node }) => {
  const currentColor = graph.getNodeAttribute(node, "color");
  const newColor = currentColor === "#f00" ? "#ff0" : "#f00";
  graph.setNodeAttribute(node, "color", newColor);
});
