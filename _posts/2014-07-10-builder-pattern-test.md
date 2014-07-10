---
layout: post
title: "Builder Pattern Test"
description: ""
category: 
tags: []
---
{% include JB/setup %}
    public class builderTest {
    private String name;
    private String sex;
    private int age;
    private float height;
    private float weight;

    public static void main(String[] args) {
        builderTest bt = new builderTest.Builder("ben","Male").age(33).height(180.00f).weight(65.00f).build();
        System.out.println(bt.name);
    }
    public static class Builder{
        private String name;
        private String sex;
        private int age = 0;
        private float height = 0;
        private float weight = 0;

        public Builder(String name, String sex) {
            this.name = name;
            this.sex = sex;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }
        public Builder height(float myHeight) {
            this.height = myHeight;
            return this;
        }

        public Builder weight(float myWeight) {
            this.weight = myWeight;
            return this;
        }
        public builderTest build(){
            return new builderTest(this);
        }
    }


    private builderTest(Builder builder){
        name = builder.name;
        sex = builder.sex;
        age = builder.age;
        height = builder.height;
        weight = builder.weight;
    }

    }
