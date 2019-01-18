import codecs
###################################生成echarts的头部代码############################
def gene_head_codes(fileName,type):
    with codecs.open(fileName, "w", "utf-8") as f:
        f.write("""<!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title></title>
                     <script src="http://echarts.baidu.com/build/dist/echarts.js"></script>
                </head>
                <body>
                    <div id="main" style="width:80%;height: 500px;border: 1px solid black"></div>
                </body>
                <script type="text/javascript">
                require.config({
                    paths: {
                        echarts: 'http://echarts.baidu.com/build/dist'
                    }
                });
                
                // 使用
                require(
                    [
                        'echarts',
                        'echarts/chart/"""+type+"""',
                    ],
                    function (ec) {
                        // 基于准备好的dom，初始化echarts图表
                        var myChart = ec.init(document.getElementById('main')); 
                        """)
###################################生成echarts的尾部代码############################
def gene_tail_codes(fileName):
    with codecs.open(fileName, "a", "utf-8") as f:
        f.write("""        
                ]
            }]
        };
        // 为echarts对象加载数据 
                        myChart.setOption(option); 
                    }
                );
                </script>
                </html>""")
##################################生成词云的核心代码################################
def gene_wordCloud(fileName, title,names, values):
    gene_head_codes(fileName, "wordCloud")
    datas = []
    for i in range(0, len(names)):
        data = {'itemStyle': 'createRandomItemStyle()' }
        data['name'] = "\"" + str(names[i]) + "\""
        data['value'] = values[i]
        datas.append(data)
     ## 追加核心代码
    with codecs.open(fileName, "a", "utf-8") as f:
        f.write("""function createRandomItemStyle() {
                                    return {
                                        normal: {
                                            color: 'rgb(' + [
                                                Math.round(Math.random() * 160),
                                                Math.round(Math.random() * 160),
                                                Math.round(Math.random() * 160)
                                            ].join(',') + ')'
                                        }
                                    };
                                }
            option = {
            title: {
                text: '"""+title+"""',
                link: 'http://www.google.com/trends/hottrends'
            },
            tooltip: {
                show: true
            },
            series: [{
                name: 'Google Trends',
                type: 'wordCloud',
                size: ['80%', '80%'],
                textRotation : [0, 45, 90, -45],
                textPadding: 0,
                autoSize: {
                    enable: true,
                    minSize: 14
                },
                data: [
                    """)
        for row in datas:  # 对于双层列表中的数据
            f.writelines(str(row).replace("'", ''))
            f.writelines(",\n")
    gene_tail_codes(fileName)