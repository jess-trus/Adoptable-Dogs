d3.csv('data/state_dog.csv', function(err, rows){
  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]});
}

var data = [{
      type: "treemap",
      path: ['age','size','breed_primary','sex','name','url'], title:"Dogs by Age"
    }];

Plotly.newPlot('plots', data);
})