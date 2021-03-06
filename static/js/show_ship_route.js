//初始化echarts实例
$(document).ready(function(){
var myChart = echarts.init(document.getElementById('main'));

var portCoord = {
	'AEJEA':[55.052065,25.00328],
	'AEDXB':[55.293775,25.27754],
	'AEMZD':[54.363355,24.52089],
	'AEAMF':[54.439685,24.33506],
	'AUDAM':[116.6732,-20.632725],
	'CNQDG':[120.3201,36.05661],
	'AUGLT':[151.2295,-23.8176],
	'SGSIN':[103.75445,1.2593655],
	'AUPHE':[118.576,-20.3165],
	'AUPWL':[117.1879,-20.6045],
	'AUHPT':[149.3073,-21.269515]
}

var Routes = [
	{port:['AEJEA','AEDXB'],route_name:'AUHPT-SGSIN',value:0.5,coord:[[55.27861,25.26711],[55.2786,25.26714],[55.27859,25.26713],[55.27863,25.26711],[55.27863,25.2671],[55.27859,25.2671],[55.27863,25.26713],[55.27862,25.26711],[55.27861,25.2671],[55.27864,25.26714],[55.27859,25.26711],[55.27864,25.26712],[55.27862,25.26712],[55.27866,25.26714],[55.27859,25.26712],[55.27862,25.26713],[55.27861,25.26714],[55.27863,25.26712],[55.27862,25.26715],[55.27859,25.26714],[55.27847,25.26699],[55.27847,25.26697],[55.27843,25.26699],[55.27841,25.26697],[55.27846,25.26697],[55.27843,25.26698],[55.27848,25.26702],[55.27845,25.26699],[55.27845,25.267],[55.27849,25.26702],[55.27845,25.26698],[55.27843,25.26701],[55.27846,25.267],[55.27844,25.267],[55.27847,25.26702],[55.27841,25.26702],[55.27845,25.26703],[55.27842,25.267]]},
	{port:['AEMZD','AEAMF'],route_name:'AUHPT-SGSIN',value:3,coord:[[54.43177,24.28523],[54.43175,24.28524],[54.43122,24.28494],[54.43123,24.28494],[54.43121,24.28493],[54.43099,24.28502],[54.43103,24.28496],[54.43101,24.28495],[54.43194,24.28534],[54.43189,24.28531],[54.43191,24.28533],[54.43189,24.28536],[54.43191,24.28532],[54.43193,24.28533],[54.43186,24.28532],[54.432,24.28539],[54.4319,24.28534],[54.43189,24.28534],[54.43187,24.28535],[54.43189,24.28535],[54.43196,24.28534],[54.43192,24.28535],[54.4312,24.28467],[54.43119,24.28466],[54.43119,24.28469],[54.43125,24.28469],[54.43122,24.28468],[54.43124,24.28473],[54.43121,24.28469],[54.43121,24.28465],[54.43124,24.2847],[54.4312,24.2847],[54.43122,24.2847],[54.43124,24.28474]]},
	{port:['AUDAM','CNQDG'],route_name:'AUHPT-SGSIN',value:5.5,coord:[[116.7194,-17.83455],[116.3439,-14.39647],[115.7473,-8.880716],[116.0631,-8.029716],[118.7331,-1.9804],[120.0633,13.30057],[122.4383,25.33163],[121.0383,35.7669],[120.3105,35.85002],[120.2726,35.8099],[120.2723,35.81027],[120.272,35.81098],[120.2343,36.02868],[120.2244,36.02722]]},
	{port:['AUGLT','SGSIN'],route_name:'AUHPT-SGSIN',value:1,coord:[[152.3586,-22.94931],[151.3062,-8.757348],[147.8406,-6.000943],[144.7165,-3.473142],[139.1779,-1.381587],[137.2194,-0.8022934],[125.7825,-3.480188],[123.0359,-7.086411],[117.4926,-7.887705],[115.0816,-7.156538],[107.4039,-0.9059883]]},
    {port:['AUPHE','CNQDG'],route_name:'AUHPT-SGSIN',value:8,coord:[[118.529,-19.29644],[119.7205,-15.73483],[121.8628,-11.83461],[122.4386,-10.78397],[125.5458,-5.680095],[126.6627,-1.663047],[127.21,1.886907],[127.863,6.296635],[127.5678,10.05243],[126.2106,26.68169]]},//[120.2483,35.78831],[120.2431,35.78548],[120.2496,35.78517],[120.2345,36.02865],[118.6693,-17.76604],[120.3148,-14.66392],[123.0978,-9.758712],[125.7747,-3.134373],[126.651,-1.113413],[127.7438,7.803355]]},
	//
    {port:['AUPWL','CNQDG'],route_name:'AUHPT-SGSIN',value:2.5,coord:[[123.8878,30.86575],[122.2879,34.60878],[120.2661,35.83116],[120.2342,36.02868],[120.2244,36.02724],[120.2244,36.02727]]},//[119.1507,-16.76225],[121.2303,-12.95139],[124.4432,-8.86217],[125.4857,-5.943847],[127.5556,10.10751],[120.2464,35.78082],[120.2245,36.02724],[120.2244,36.02725]]},
	{port:['AUHPT','SGSIN'],route_name:'AUHPT-SGSIN',value                                                                                                                                                                                                                                                                                                                                                                                                                                                                      :10,coord:[[150.4568,-19.6733],[151.4757,-15.81073],[151.9697,-12.32122],[151.0539,-8.135533],[147.6091,-5.772133],[144.4588,-3.303717],[141.6017,-1.792867],[136.6603,0.79544],[132.6886,2.868433],[125.4193,5.273],[115.6311,7.190467],[115.6257,7.18915],[103.9362,1.2678]]}
	];
option = null;

//指定图表的配置项和数据
var convertData = function (one_route) {
    var res = [];
	var data = one_route.coord;
	var value = one_route.value;
	res.push({coords:[portCoord[one_route.port[0]],data[0]],value:value});
    for (var i = 0; i < data.length-1; i++) {
        //var dataItem = data[i];
		//var leaveCoord = portCoord[one_route.leave_port];
		//var arriveCoord = portCoord[one_route.arrive_port];
        var fromCoord = data[i];
        var toCoord = data[i+1];
        if (fromCoord && toCoord) {
            res.push({
                //fromName: dataItem[0].name,
                //toName: dataItem[1].name,
                coords: [fromCoord, toCoord],
				value:value
            });
        }
    }
	res.push({coords:[data[data.length-1],portCoord[one_route.port[1]]],value:value});
    return res;
};

var toPoint = function(one_route){
	var res = [];
	var data = one_route.port;
	var value = one_route.value;
    for (var i = 0; i < data.length; i++) {
        var geoCoord = portCoord[data[i]];
        if (geoCoord) {
            res.push({
                name: data[i],
                value: geoCoord.concat(value)
            });
        }
    }
    return res;
}

//var color = ['#a6c84c', '#ffa022', '#46bee9'];
var series = [];
for(var i=0; i<Routes.length; i++){
	series.push({
			name: Routes[i].route_name,
			type: 'lines',
			coordinateSystem: 'bmap',
			zlevel: 2,
			lineStyle: {
				normal: {
					//color: color[Routes[i].value],
					width: 2,
					opacity:1,
					curveness: -0.05
				}
			},
			data: convertData(Routes[i])
	},
	{
		//name:'Port:' + Routes[i].leave_port,
		type:'scatter',
		coordinateSystem: 'bmap',
        zlevel: 2,
		symbolSize: 5,
		label: {
            normal: {
                show: false
            },
            emphasis: {
                show: false
            }
        },
        itemStyle: {
            emphasis: {
                borderColor: '#fff',
                borderWidth: 1
            }
        },
        data: toPoint(Routes[i])
	}
	);
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
        center: [0,0],
        zoom: 1,
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
	
	dataRange: {
        min: 0,
        max: 10,
        x: 'left',
        calculable: true,
        color: ['red', 'orange', 'yellow', 'lime', 'aqua'],
        textStyle: {
            color: '#fff'
        }
    },
	series:series
};

    // 使用刚指定的配置项和数据显示图表。
	if (option && typeof option === "object") {
		myChart.setOption(option, true);
	}
	});