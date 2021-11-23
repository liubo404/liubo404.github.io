---
layout: post
title: "start flow"
description: ""
category: wrk
tags: [test]
---
{% include JB/setup %}


```
wrk  -t4 -c15 -d30s -s startFlow.lua http://172.16.101.209:9001/process/start

```

- startfFlow.lua 

```
math.randomseed(os.time())
number =  math.random()

wrk.headers["Content-Type"] = "application/json"
wrk.headers["X-ACCESS-TOKEN"] = "HZJGH9l9kf5n3r4svyWwV68e3XYpm4ob14MRub1s"

wrk.method = "POST"
wrk.body = '
{
    "data": {
        "item_no": "A00000"+tostring(number),
        "item_type": "1409842915260760066",
        "title": "调研出差",
        "fee_total": 123,
        "ticket_count": 0,
        "before_id": null,
        "fee_data": [
            {
                "id": "1460448468844208129",
                "amount": 123,
                "feeType": "1408724828877365555",
                "type": 1,
                "standard": 0,
                "feeId": "1408724828877365555"
            }
        ],
        "reimburser_id": "1411161953669292034"
    },
    "formDataId": "",
    "id": "1457623833849761792"
}
'
```

## final version
```
counter = 0
request = function()
    path = "http://172.16.101.209:9001/process/start"
    math.randomseed(os.time())
    counter = counter + 1
    number =  math.random() + counter

    wrk.headers["Content-Type"] = "application/json"
    wrk.headers["X-ACCESS-TOKEN"] = "1J_rY3iuUZvwGyBur_E7GzdBcM586q0V75__"

    wrk.method = "POST"
    wrk.body = '{"data":{"item_no":"AO000' .. tostring(number) .. '","item_type":"1409842915260760066","title":"调研出差","fee_total":123,"ticket_count":0,"before_id":null,"fee_data":[{"id":"1460448468844208129","amount":123,"feeType":"1408724828877365555","type":1,"standard":0,"feeId":"1408724828877365555"}],"reimburser_id":"1411161953669292034"},"formDataId":"","id":"1457623833849761792"}'
    return wrk.format(nil,path)
end
```

- example.1

```lua
wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"
wrk.headers["X-ACCESS-TOKEN"] = "Yc_uZ7HaoTClA5Mb3_aOmSHEpy9ilpAGrr__" 
wrk.body = '{ "id": 1424561068952391680,  "data": {  "item_no": "202103111031001",   "dept_id": 1382246160558727169, "handler_id": 1411162010313367554,    "form_type": 1413003164780728320,   "item_type": 1410836523636060162,    "title": "demo.23",    "plan_fee_data": [{"title":"圆珠笔","number":9,"price": 5 ,"subtotal": 45},{"title":"打印纸","number":3,"price": 10 ,"subtotal": 30}],    "total": 75,    "money": 2000.23,    "approval_doc": [      "abc/sss/sss/a.txt",      "ssd/ss/b.jpg"    ],    "notify_file": [      "aa/a.doc",      "bb/b.excel"    ]  }}'

```

- example.2

```lua

 io.open("start.json", "r")

wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"
wrk.headers["X-ACCESS-TOKEN"] = "Yc_uZ7HaoTClA5Mb3_aOmSHEpy9ilpAGrr__" 
wrk.body = io.read()
```

- exmple.3

```lua
wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"
wrk.headers["X-ACCESS-TOKEN"] = "ba_3HFArpHss5Y1Mf_mzfU6EzDaw0PdUjb__" 
wrk.body = '{"data":{"item_no":"AO2110080138","item_type":"1417406392775008258","title":"办公经费wrk","fee_total":1,"ticket_count":0,"before_id":null,"fee_data":[{"id":"1446407502621581314","amount":1,"feeType":"1408724866311524352","type":1,"standard":0,"feeId":"1408724866311524352"}],"reimburser_id":"1411161953669292034"},"formDataId":"","id":"1442307637898252288"}'

```

test.json 

```json
{
  "id": 1424561068952391680,
  "data": {
    "item_no": "202103111031001",
    "dept_id": 1382246160558727169,
    "handler_id": 1411162010313367554,
    "form_type": 1413003164780728320,
    "item_type": 1410836523636060162,
    "title": "demo网关.或.24",
    "plan_fee_data": [{"title":"圆珠笔","number":9,"price": 5 ,"subtotal": 45},{"title":"打印纸","number":3,"price": 10 ,"subtotal": 30}],
    "total": 75,
    "money": 2000.23,
    "approval_doc": [
      "abc/sss/sss/a.txt",
      "ssd/ss/b.jpg"
    ],
    "notify_file": [
      "aa/a.doc",
      "bb/b.excel"
    ]
  }
}

```

## jmeter jmx

```
jmeter.sh  -n -t  ./startFlow.jmx -l s1.jtl -e -o ./report/
```

```xml
 
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0" jmeter="5.3">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="Test Plan" enabled="true">
      <stringProp name="TestPlan.comments"></stringProp>
      <boolProp name="TestPlan.functional_mode">false</boolProp>
      <boolProp name="TestPlan.tearDown_on_shutdown">true</boolProp>
      <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
        <collectionProp name="Arguments.arguments"/>
      </elementProp>
      <stringProp name="TestPlan.user_define_classpath"></stringProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <stringProp name="LoopController.loops">1</stringProp>
        </elementProp>
        <stringProp name="ThreadGroup.num_threads">1</stringProp>
        <stringProp name="ThreadGroup.ramp_time">1</stringProp>
        <boolProp name="ThreadGroup.scheduler">false</boolProp>
        <stringProp name="ThreadGroup.duration"></stringProp>
        <stringProp name="ThreadGroup.delay"></stringProp>
        <boolProp name="ThreadGroup.same_user_on_next_iteration">true</boolProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP Request" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">&#xd;
{&#xd;
  &quot;id&quot;: 1424561068952391680,&#xd;
  &quot;data&quot;: {&#xd;
    &quot;item_no&quot;: &quot;202103111031001&quot;,&#xd;
    &quot;dept_id&quot;: 1382246160558727169,&#xd;
    &quot;handler_id&quot;: 1411162010313367554,&#xd;
    &quot;form_type&quot;: 1413003164780728320,&#xd;
    &quot;item_type&quot;: 1410836523636060162,&#xd;
    &quot;title&quot;: &quot;demo.gw.and.18&quot;,&#xd;
    &quot;plan_fee_data&quot;: [{&quot;title&quot;:&quot;圆珠笔&quot;,&quot;number&quot;:9,&quot;price&quot;: 5 ,&quot;subtotal&quot;: 45},{&quot;title&quot;:&quot;打印纸&quot;,&quot;number&quot;:3,&quot;price&quot;: 10 ,&quot;subtotal&quot;: 30}],&#xd;
    &quot;total&quot;: 75,&#xd;
    &quot;money&quot;: 2000.23,&#xd;
    &quot;approval_doc&quot;: [&#xd;
      &quot;abc/sss/sss/a.txt&quot;,&#xd;
      &quot;ssd/ss/b.jpg&quot;&#xd;
    ],&#xd;
    &quot;notify_file&quot;: [&#xd;
      &quot;aa/a.doc&quot;,&#xd;
      &quot;bb/b.excel&quot;&#xd;
    ]&#xd;
  }&#xd;
}&#xd;
</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">172.16.101.209</stringProp>
          <stringProp name="HTTPSampler.port">9001</stringProp>
          <stringProp name="HTTPSampler.protocol">http</stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">/process/start</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree>
          <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
            <collectionProp name="HeaderManager.headers">
              <elementProp name="" elementType="Header">
                <stringProp name="Header.name">X-ACCESS-TOKEN</stringProp>
                <stringProp name="Header.value">1J_9WIOyfD2JqpCKC_Dz5k1NCcRwdrTOc3__</stringProp>
              </elementProp>
              <elementProp name="" elementType="Header">
                <stringProp name="Header.name">Content-Type</stringProp>
                <stringProp name="Header.value">application/json</stringProp>
              </elementProp>
            </collectionProp>
          </HeaderManager>
          <hashTree/>
        </hashTree>
        <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree" enabled="true">
          <boolProp name="ResultCollector.error_logging">false</boolProp>
          <objProp>
            <name>saveConfig</name>
            <value class="SampleSaveConfiguration">
              <time>true</time>
              <latency>true</latency>
              <timestamp>true</timestamp>
              <success>true</success>
              <label>true</label>
              <code>true</code>
              <message>true</message>
              <threadName>true</threadName>
              <dataType>true</dataType>
              <encoding>false</encoding>
              <assertions>true</assertions>
              <subresults>true</subresults>
              <responseData>false</responseData>
              <samplerData>false</samplerData>
              <xml>false</xml>
              <fieldNames>true</fieldNames>
              <responseHeaders>false</responseHeaders>
              <requestHeaders>false</requestHeaders>
              <responseDataOnError>false</responseDataOnError>
              <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
              <assertionsResultsToSave>0</assertionsResultsToSave>
              <bytes>true</bytes>
              <sentBytes>true</sentBytes>
              <url>true</url>
              <threadCounts>true</threadCounts>
              <idleTime>true</idleTime>
              <connectTime>true</connectTime>
            </value>
          </objProp>
          <stringProp name="filename"></stringProp>
        </ResultCollector>
        <hashTree/>
      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>

```