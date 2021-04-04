function donughtchart(text, data) {

    var DonughtChart = new CanvasJS.Chart("DonughtChart",
        {
            title: {
                text: text, //"Polarity Count",
                fontFamily: "Impact",
                fontWeight: "normal"
            },

            legend: {
                verticalAlign: "bottom",
                horizontalAlign: "center"
            },
            data: [
                {
                    startAngle: 45,
                    indexLabelFontSize: 20,
                    indexLabelFontFamily: "Garamond",
                    indexLabelFontColor: "darkgrey",
                    indexLabelLineColor: "darkgrey",
                    indexLabelPlacement: "outside",
                    type: "doughnut",
                    showInLegend: true,
                    dataPoints:data
                    // dataPoints: data [
                    //     { y: posValues.length, legendText: "Positive Values " + (posValues.length / total * 100).toFixed(2) + "%", indexLabel: "Positive Values " + (posValues.length / total * 100).toFixed(2) + "%" },
                    //     { y: negValues.length, legendText: "Negative Values " + (negValues.length / total * 100).toFixed(2) + "%", indexLabel: "Negative Values " + (negValues.length / total * 100).toFixed(2) + "%" },
                    //     { y: neuValues.length, legendText: "Neutral Values " + (neuValues.length / total * 100).toFixed(2) + "%", indexLabel: "Neutral Values " + (neuValues.length / total * 100).toFixed(2) + "%" }
                    // ]
                }
            ]
        });
    DonughtChart.render();
}


