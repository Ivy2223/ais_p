//初始化echarts实例
var myChart = echarts.init(document.getElementById('container'));
var Routes = [
	{route_name:'AEAMF-AEAMF',value:3,coord:[[54.5,24.3],[54.1,24.7],[53.5,24.0],[52.45883,24.35154],[52.45985,24.35515]]},
	{route_name:'AEDAS-AEDAS',value:2,coord:[[52.89137,25.13948],[53.5,25.13943],[53.891,25.5394],[53.99,25.1],[53.3,24.5]]},
	{route_name:'AEJEA-AEDXB',value:1,coord:[[55.26105,26.26858],[55.0,26.0],[54.25986,25.26805],[54.2611,25.0],[54.0,25.5]]}

	];

option = null;

//指定图表的配置项和数据
var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length-1; i++) {
        //var dataItem = data[i];
        var fromCoord = data[i];
        var toCoord = data[i+1];
        if (fromCoord && toCoord) {
            res.push({
                //fromName: dataItem[0].name,
                //toName: dataItem[1].name,
                coords: [fromCoord, toCoord]
            });
        }
    }
    return res;
};

var color = ['#a6c84c', '#ffa022', '#46bee9'];
var series = [];
for(var i=0; i<Routes.length; i++){
	series.push({
			name: Routes[i].route_name,
			type: 'lines',
			coordinateSystem: 'bmap',
			zlevel: 2,
			lineStyle: {
				normal: {
					color: color[Routes[i].value],
					width: Routes[i].value,
					opacity:1,
					curveness: 0.1
				}
			},
			data: convertData(Routes[i].coord)
	});
}


option = {
    title : {
        text: '全球航线图',
        left: 'center',
        textStyle : {
            color: '#fff'
        }
    },
    tooltip : {
        trigger: 'item'
    },
	//百度地图
    bmap: {
        center: [54,25],
        zoom: 10,
        roam: true,
		mapStyle: {
            styleJson: [
                    {
                        "featureType": "water",
                        "elementType": "all",
                        "stylers": {
                            "color": "#044161"
                        }
                    },
                    {
                        "featureType": "land",
                        "elementType": "all",
                        "stylers": {
                            "color": "#004981"
                        }
                    },
                    {
                        "featureType": "boundary",
                        "elementType": "geometry",
                        "stylers": {
                            "color": "#064f85"
                        }
                    },
                    {
                        "featureType": "railway",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "highway",
                        "elementType": "geometry",
                        "stylers": {
                            "color": "#004981"
                        }
                    },
                    {
                        "featureType": "highway",
                        "elementType": "geometry.fill",
                        "stylers": {
                            "color": "#005b96",
                            "lightness": 1
                        }
                    },
                    {
                        "featureType": "highway",
                        "elementType": "labels",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry",
                        "stylers": {
                            "color": "#004981"
                        }
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry.fill",
                        "stylers": {
                            "color": "#00508b"
                        }
                    },
                    {
                        "featureType": "poi",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "green",
                        "elementType": "all",
                        "stylers": {
                            "color": "#056197",
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "subway",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "manmade",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "local",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "labels",
                        "stylers": {
                            "visibility": "off"
                        }
                    },
                    {
                        "featureType": "boundary",
                        "elementType": "geometry.fill",
                        "stylers": {
                            "color": "#029fd4"
                        }
                    },
                    {
                        "featureType": "building",
                        "elementType": "all",
                        "stylers": {
                            "color": "#1a5787"
                        }
                    },
                    {
                        "featureType": "label",
                        "elementType": "all",
                        "stylers": {
                            "visibility": "off"
                        }
                    }
            ]
        }
    },

	series:series
};

    // 使用刚指定的配置项和数据显示图表。
	if (option && typeof option === "object") {
		myChart.setOption(option, true);
	}