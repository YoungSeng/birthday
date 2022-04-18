// 霸都丶傲天 2019年10月10日 https://github.com/AJLoveChina/birthday
var config = {
    // 句子的长度可以任意， 你可以写十句话， 二十句话都可以
    // 每句话尽量不要超过15个字,不然展示效果可能不太好
    texts: [
        "送给我",      //这里,每句话结尾的最后一个逗号必须是英文的哦!! 很重要哦!!
        "心爱的小可爱",  // 同上...
        "今天是你的生日",
        "这是我们在一起的",
        "第二个生日了哦",
        "今年要吃好的喽哦",
        "要把我家可爱猪猪喂饱饱",
        "然后抱走",
        "愿你贪吃不胖",
        "愿你懒惰不丑", 
        "愿你永远健康美好依旧", 
        "愿你从旧衣服找到零钱",  
        "愿你做过的美梦全都实现",  
        "愿你永远都有好运气", 
        "原这岁月悠长", 
        "我们即使不见亦能不散", 
        "若这一切太难", 
        "我只愿你一生简单", 
        "一生平安！ ", 
        "不是生日,也要快乐", 
        "是生日,更要快乐", 
        "2022.4.16", 
    ],
    /**
     * imgs 可以不填, 但是如果要填写的话必须遵循下面的格式
     * "对应上面的文字, 要完全一样" : "图片地址, 可以把图片放在imgs文件夹中"
     * 例如
     * "心爱的小可爱": "./imgs/xiaokeai.jpg"
     *
     * 如果不要图片的话, 直接在每行开头写两个斜杠注释即可, 例如下面的 "今天是你的生日" 的图片就不会展示了:)
     * Tip: 图片最好用正方形or接近正方形, 看起来效果更好
     */
    imgs: {
        "心爱的小可爱": "./imgs/Screenshot_20220302_124932_com.tencent.mm.jpg",
         "今天是你的生日": "./imgs/Screenshot_20211228_110945_com.tencent.mm.jpg",
        "这是我们在一起的": "./imgs/Screenshot_20211228_112541_com.tencent.mm.jpg",
        "第二个生日了哦": "./imgs/Screenshot_20211231_225929_com.tencent.mm.jpg",
        "今年要吃好的喽哦": "./imgs/Screenshot_20220101_000119_com.tencent.mm.jpg",
        "要把我家可爱猪猪喂饱饱": "./imgs/Screenshot_20220108_141049_com.tencent.mm.jpg",
        "然后抱走": "./imgs/Screenshot_20220130_005729_com.tencent.mm.jpg",
        "愿你贪吃不胖": "./imgs/Screenshot_20220131_003925_com.tencent.mm.jpg",
        "愿你懒惰不丑”: "./imgs/Screenshot_20220131_124542_com.tencent.mm.jpg",
        "愿你永远健康美好依旧": "./imgs/Screenshot_20220202_221748_com.tencent.mm.jpg", 
        "愿你从旧衣服找到零钱": "./imgs/Screenshot_20220203_161210_com.tencent.mm.jpg", 
        "愿你做过的美梦全都实现": "./imgs/Screenshot_20220204_193835_com.tencent.mm.jpg", 
        "愿你永远都有好运气": "./imgs/Screenshot_20220205_180434_com.tencent.mm.jpg", 
        "原这岁月悠长": "./imgs/Screenshot_20220219_232806_com.tencent.mm.jpg",
        "我们即使不见亦能不散": "./imgs/Screenshot_20220222_182953_com.tencent.mm.jpg", 
        "若这一切太难": "./imgs/Screenshot_20220222_224200_com.tencent.mm.jpg",
        "我只愿你一生简单": "./imgs/Screenshot_20220228_171129_com.tencent.mm.jpg",
        "一生平安！ ": "./imgs/Screenshot_20220301_191419_com.tencent.mm.jpg",
        "不是生日,也要快乐": "./imgs/Screenshot_20220301_191745_com.tencent.mm.jpgg",
        "是生日,更要快乐": "./imgs/Screenshot_20220302_124820_com.tencent.mm.jpg",
        // "今天是你的生日": "./imgs/birthday.jpg",
    },
    // 按钮文字描述, 以下是默认的按钮文字，英文的，您可以改成你喜欢的文字
    desc: {
        turn_on: "开始",
        play: "音乐",
        bannar_coming: "氛围",
        balloons_flying: "好像少点东西",
        cake_fadein: "蛋糕？",
        light_candle: "蜡烛？",
        wish_message: "生日快乐",
        story: "A MESSAGE FOR YOU",
    }
};
