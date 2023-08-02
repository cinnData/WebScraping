# Project - Get a look from Zalando

## Introduction

**Zalando SE** is a German multinational e-commerce company based in Berlin, with headquarters in Berlin and tech hubs in Dublin, Dortmund and Helsinki. Zalando is, right now, the Europe's biggest online-only fashion retailer. It follows a platform approach, offering fashion and lifestyle products to customers in 23 European markets. 

Zalando was founded in Germany in 2008. Since 2013, following examples of tech companies from the East, especially China, Zalando transitioned into a European digital platform. Emulating Chinese companies, Zalando set off into remaking itself into a digital shopping mall, allowing fashion houses and retailers to make sales via the Partner Program as well, often with limited input from Zalando. 

Zalando webpage in Spain is `zalando.es`. There are also separate pages for woman (`zalando.es/mujer-home`), man (`zalando.es/hombre-home`) and children (`zalando.es/nino-home`). Selecting the option *Get the look*, you access the page ` zalando.es/consigue-el-look-mujer`. There, you can find pictures of influencers, called at Zalando **creators**, showing their **looks**. 

Every picture has a link, which leads you to the look's page, and the name of the creator has another link which sends you the creator's page. For instance, the top left look (right now) is due to a creator called *babicatarine*, guilty of 9 looks. Clicking on the picture, you are sent to the page `zalando.es/outfits/47f4juSETte`, which displays information on the articles that make the look. Clicking on the name of the creator, you are sent to `zalando.es/creator/5920069a-7a73-4476-a74f-29488ab83a6f`, which contains information on the creator.

Extracting information from this page has a specific problem not yet discussed in this course. After accepting cookies, you get a page which does not contain all the looks. More specifically, it contains 48 looks provided either by creators, by Zalando itself, or by brands such as Timberland and Coach. But the way you get the rest of the looks is not by clicking on a button, but by scrolling to the bottom of the page. You may have to scroll down more than 20 times to get the whole collection. By makig choices such as 'Clásico', 'Casual', 'Streetwear', etc, you get subcollections, for which less scrolling is needed. With **Selenium**, we can control the scrolling from a Python kernel.

## The target data

The objective of this example is to collect information on the looks posted at `zalando.es/consigue-el-look`\break`-mujer` and the creators involved, exporting it to a tabular file, in which every row corresponds to a look. We aim at capturing the following fields:

* `img_link`, the link to the picture of that look. Example: `img01.ztat.net/outfit/fb037c3314fd43f`\break`39141aaac85cd0828/da54a6d554db40c2b4ed5202a75beaa5.jpg?imwidth=600`.

* `out_link`, the link to the the page of that look, which displays information on the articles that make the look. Example: `zalando.es/outfits/47f4juSETte`.

* `creator`, the creator's name. Example: 'babicatarine'.

* `cre_link`, the link to the the page of the creator of that look, which contains information on the creator. Example: `zalando.es/creator/5920069a-7a73-4476-a74f-29488ab83a6f`.
