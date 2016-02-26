/**
 * Created by Yueqi on 2/23/2016.
 */
var setting = {
    tids: [],
    c_index: 0,
    index: 0,
    tid: 4,
    mid: 60069,
    m_index: {}
}

//load detail view
var width =400,
    height= 400,
    ox = d3.scale.linear().range([0, width]),
    oy = d3.scale.linear().range([height, 0]);

function initial_overview(callback){
        //initial overview
    d3.json('overview', function(data){
        for (var i in data){
            data[i].topic = {}
        }
        ox.domain([d3.min(data, function(d){return d.x}), d3.max(data, function(d){return d.x})])
        oy.domain([d3.min(data, function(d){return d.y}), d3.max(data, function(d){return d.y})])

        var svg = d3.select('#overview-wrap').append('svg')
            .attr('viewBox','0 0 '+width+' '+height)
            .style('height','100%')
            .style('width','100%')
            .append('g').attr('id','overview_wrap');

        var over = svg.selectAll('pos')
            .data(data).enter()
            .append('g')
            .attr('class','over')
            .attr('id', function(d){
                return 'over-'+ d.mid
            })
            .attr('transform',function(d){
                return 'translate('+ox(d.x)+','+oy(d.y)+')'
            });

        over.append('circle')
            .attr('cx',0)
            .attr('cy',0)
            .attr('r', 1)
            .attr('fill','lightgray');

        over.append('text').text('')

        if (callback)
            callback()
    })
}

function start(){
    visited_topic = {}
    $.get('set?mid='+setting.mid+'&tid='+setting.tid, function(){
        d3.json('topic_list', function(d){
            //add two empty topic
            d.push({ tid: -1 });
            d.unshift({ tid: -1 });

            setting.tids = d;

            var pos = 0
            for (var i in d){
                if (d[i].tid == setting.tid){
                    pos = parseInt(i);
                    setting.c_index = pos;
                    setting.index = pos;
                    break
                }
            }
            d3.select('#wrap').html('');
            var topic = d3.select('#wrap')
                .selectAll('topic').data(setting.tids).enter()
                .append('div')
                .attr('id', function(d,i){
                    return 'topic-'+i
                })
                .attr('class', 'topic')

            $('.topic').hide()

            //the center trail should already been loaded
            load_items(setting.index, function(){
                $('#topic-'+(setting.index)).show()
                show_topic_in_overview(setting.tids[pos].tid)
            })

            //load up and down trails
            load_items(setting.index-1, function(){
                //get snap for the first five items
                $('#topic-'+(setting.index-1)).show()
            });
            load_items(setting.index+1, function(){
                $('#topic-'+(setting.index+1)).show()
            })

            load_movie_detail()
        })
    })
}

function load_movie_detail(){
    //load select movie details
    $('#detail').load('detail?mid='+setting.mid, function(){

        // draw topic overview
        d3.select('#topic_overview')
            .html('')
            .append('svg')
            .style('height', '100%')
           .attr('viewBox','0 0 40 360')
           .selectAll('circle')
           .data(setting.tids).enter()
           .append('circle')
           .attr('class', 'topicover')
           .attr('cx', 20)
           .attr('cy', function(d, i){
               return 40*i+20
           })
           .attr('r', function(d){
                if (d.tid >= 0)
                    return r_size(d.weight)
                else
                    return 0
           })
           .attr('stroke','black')
        update_topic_overview()
    });
}

//input tid
var visited_topic = {};

var top = 10,
    r_size = d3.scale.linear().range([5, 20]).domain([3, 2000])

function show_topic_in_overview(tid){
    // highlight in overview
    var node = d3.selectAll('.over');
    node.select('circle')
        .attr('r', function(d){
            if (tid in d.topic)
                return r_size(d.topic[tid].w)
            else
                return 1
        })
    node.select('text')
        .text(function(d){
            if (tid in d.topic && d.topic[tid].i < top){
                return d.title
            }
            else{
                return ''
            }
        })
}

//load detail info to overview
function load_items(index, callback){
    //index = (index + setting.tids.length) % setting.tids.length
    var tid = setting.tids[index].tid
    if (tid >=0 && tid in visited_topic){
        if (callback)
            callback();
        return
    }
    d3.json('item_list?tid='+tid, function(data){
        // assign weight to overview
        //tag top 5 (response order by weight)
        for (var i in data){
            d3.select('#over-'+data[i].mid)
                .each(function(d){
                    d.load = false
                    d.title = data[i].title
                    d.topic[tid] = {
                        w:data[i].weight,
                        i:i
                    }
                })
        }
        //order by order
        data.sort(function(a,b){
            if (b.order == a.order)
                return b.weight - a.weight
            else
                return b.order - a.order
        });

        visited_topic[tid] = data;

        //add to topic chain

        d3.select('#topic-'+index)
            .selectAll('item').data(data).enter()
            .append('div')
            .text(function(d){return d.mid})
            .attr('class','item')
            .on('click', function(d){
                visit(d.mid, tid)
            })
            .classed('visit', function(d){
                return d.visited
            });

        //the initial index
        setting.m_index[index] = 0;
        //load first 7 items after start index
        d3.selectAll('#topic-'+index+' .item').each(function(d, i){
            if (i<9 && !d.load){
                d.load = true;
                $(this).load('snap?mid='+ d.mid)
            }
        });
        if (callback)
            callback()
    })
}

//only animations
var duration = 500,
    up = { direction: 'up'},
    down = { direction: 'down'}

function set_interaction(){
    $('body').keydown(function(event){
        console.log(event.which)
        switch (event.which){
            //up:
            case 38:
                if (setting.index < setting.tids.length-2){
                    setting.index += 1;
                    load_items(setting.index+1, function(){
                        $('#topic-'+(setting.index-2)).slideUp(duration)
                        $('#topic-'+(setting.index+1)).slideDown(duration)
                    })
                    update_topic_overview()
                    show_topic_in_overview(setting.tids[setting.index].tid);
                }
                break;
            //down:
            case 40:
                if (setting.index>1) {
                    setting.index -= 1;
                    load_items(setting.index - 1, function () {
                        $('#topic-' + (setting.index + 2)).slideUp(duration)
                        $('#topic-' + (setting.index - 1)).slideDown(duration)
                    })
                    update_topic_overview()
                    show_topic_in_overview(setting.tids[setting.index].tid);
                }
                break;
            //left (people will not finish the list):
            case 37:
                d3.selectAll('#topic-'+setting.index+' .item').each(function(d, i){
                    if (i<setting.m_index[setting.index]+9 && !d.load){
                        $(this).load('snap?mid='+ d.mid)
                    }
                })
                $('#topic-'+setting.index+' .item:nth-child('+setting.m_index[setting.index]+')').animate({width: 'toggle'})
                setting.m_index[setting.index] += 1;
                break;
            //right (every item on left should have be loaded):
            case 39:
                if (setting.m_index[setting.index] > 0) {
                    $('#topic-' + setting.index + ' .item:nth-child(' + (setting.m_index[setting.index] - 1) + ')').animate({width: 'toggle'})
                    setting.m_index[setting.index] -= 1
                }
                break;
        }
    })
}

function update_topic_overview(){
    d3.selectAll('.topicover').attr('fill', function(d,i){
       if (Math.abs(i-setting.index) < 2)
           return 'red'
       else
           return 'none'
    })
}

// search an item (show the topic with biggest weight)
function visit(mid){ visit(mid, -1) }

// keep the source topic
function visit(mid, tid){
    setting = {
            tids: [],
            c_index: 0,
            index: 0,
            tid: tid,
            mid: mid,
            m_index: {}
        }
    start()
}