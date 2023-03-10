# software_engineering_lab
# گزارش کار آزمایش 1

در مرحله اول ریپازیتوری مربوطه را ساخته و با دستور زیر آن را به صورت ریموت خواهیم داشت.

git remote add origin git@github.com:almaho/software_engineering_lab

git push -origin master


حالا میتوانیم با دستورات مختلف کد های جدید توسط اکانت های مختلف به ریپازیتوری اضافه کنیم.

به صورت خاص میبینید که هنگام مرج دو برنچ باید کانفلیکت های زیر را حل کنیم.
# سوال ها:
1) پوشه .git یک دایرکتوری مخفی است که زمانی که یک git repository جدید را initialize می کنیم ، به طور خودکار ایجاد می شود. و شامل تمام اطلاعات مورد نیاز git برای مدیریت و دایرکتوری فایل ها در پروژه نیاز دارد. اطلاعات مختلفی مانند تماما commit ها در repository، پایگاه داده ای از تمام فایل ها و دایرکتوری هایی که توسط Git ردیابی می شوند،branch ها و tag  هایی که نقاط خاصی را در تارخیچه repository  مشخص می کنند و اطلاعات Configuration برای repository و خود git
برای ایجاد یک پوشه .git در یک پوشه، باید دستور "git init" را در ترمینال یا Git bash خود اجرا کنید.
2) در atomic commit، تمام تغییرات باید یا به طور کامل در یک پایگاه داده یا سیستم فایل تکمیل شوند یا در صورت خرابی به طور کامل به عقب برگردند،به این دلیل که اطمینان از ثابت بودن داده ها حاصل شود و به طور دقیق تغییرات را منعکس می کنند. اما در atomic pull-request، تمام تغییرات ایجاد شده در یک branch یا commit با هم ترکیب می‌شوند و به‌عنوان یک واحد ارسال می‌شوند، تا اطمینان از این که کد می‌تواند به عنوان یک ویژگی کامل و مستق بررسی شود  قبل از اینکه ادغام در پایگاه کد اصلی اتفاق بیفتد.
3) فرمانی است که تمام آخرین تغییرات را از remote repository بهlocal repository می آورد. هر commit، شاخه و تگ جدید را دانلود می کند اما آنها را در پایگاه کد شما گنجانده نمی شود.

دستور Pull دو عملیات fetch و merge را ترکیب می کند. تغییرات را از remote repository دریافت می کند و بلافاصله آنها را در شاخه فعلی شما ادغام می کند. پس از دانلود تغییرات، به طور خودکار آنها را در پایگاه کد شما اعمال می کند.

Merge فرمانی است که تغییرات را از یک شاخه به شاخه دیگر ادغام می کند. این دو مجموعه از تغییرات کد را که در دو شاخه مختلف ایجاد شده اند ترکیب می کند. ادغام زمانی اتفاق می افتد که بخواهید تغییرات ایجاد شده در یک شاخه را در شاخه دیگری ترکیب کنید

4) دستور Reset برای خنثی سازی یک سری از commit هایی که به repository انجام شده است استفاده می شود. این دستور نشانگر branch را به یک commit دیگر منتقل می کند و دایرکتوری کاری یا ناحیه مرحله بندی را تغییر نمی دهد.

دستور Revert برای برگرداندن یک یا چند commit استفاده می شود. یک commit جدید ایجاد می کند که تغییرات ایجاد شده در commit های مشخص شده را خنثی می کند. Revert تاریخچه commit موجود را تغییر نمی دهد. یک commit جدید اضافه می کند که commit قبلی را معکوس می کند.

دستور Rebase برای تغییر پایه یک branch استفاده می شود. کل branch را به یک نقطه شروع جدید منتقل می کند، که می تواند در همان شاخه یا یک شاخه متفاوت باشد. Rebase برای ترکیب تغییرات از یک branch بالادستی که جلوتر از شاخه فعلی است استفاده می شود.

دستور Restore برای بازگرداندن محتویات یک فایل یا دایرکتوری به حالت قبلی استفاده می شود. هر تغییری که از زمان commit مشخص شده در فایل یا دایرکتوری ایجاد شده را حذف می کند و محتویات را به حالت آن commit باز می گرداند. از Restore می توان برای بازیابی فایل های از دست رفته یا آسیب دیده استفاده کرد.

به طور خلاصه، Reset و Revert برای لغو تغییرات، Rebase برای جابجایی پایه یک شاخه و Restore برای بازیابی فایل های از دست رفته یا آسیب دیده استفاده می شود.
5) در stage در Git به معنای آماده سازی تغییرات ایجاد شده در فایل های موجود در repository برای انجام commit ها است. تغییرات stage شامل افزودن فایل‌های اصلاح‌شده یا فایل‌های جدید به یک منطقه stage به نام index یا cache است. پس از مرحله بندی تغییرات، آنها آماده هستند تا commit شوند و به  remote repository منتقل شوند.
از سوی دیگر، دستور stash در Git برای ذخیره موقت تغییرات uncommitt استفاده می شود. این به ما اجازه می دهد تا بین branch ها حرکت کنند یا روی کارهای مختلف بدون انجام تغییرات کد کار کنند.


6) در Git، یک snapshot به یک کپی از کل repository در یک زمان خاص اشاره دارد. این شامل تمام فایل ها و دایرکتوری های موجود در repository در آن لحظه به همراه محتویات و metadata های آنها است. به طوری کلی وقتی یک commit در Git ایجاد می کنیم، در واقع یک snapshot از تغییرات ایجاد شده در repository از زمان commit قبلی گرفته ایم.


