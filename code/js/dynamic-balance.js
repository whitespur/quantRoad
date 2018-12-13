// 回测环境
/*backtest
start: 2018-01-01 00:00:00
end: 2018-08-01 11:00:00
period: 1m
exchanges: [{"eid":"OKCoin_EN","currency":"BTC"}]
*/



// 撤单函数
function CancelPendingOrders() {
    Sleep(1000); // 休眠 1秒
    var ret = false;
    while (true) {
        var orders = null;
        // 持续获取未成交订单数组，如果返回异常，则继续获取
        while (!(orders = exchange.GetOrders())) {
            Sleep(1000); // 休眠 1秒
        }
        if (orders.length == 0) { // 如果订单数组为空
            return ret; // 返回撤单状态
        }
        for (var j = 0; j < orders.length; j++) { // 遍历未成交订单数组
            exchange.CancelOrder(orders[j].Id); // 依次取消未成交订单
            ret = true;
            if (j < (orders.length - 1)) {
                Sleep(1000); // 休眠 1秒
            }
        }
    }
}

// 下单函数
function onTick() {
    var acc = _C(exchange.GetAccount); // 获取账户信息
    var ticker = _C(exchange.GetTicker); // 获取 Tick 数据
    var spread = ticker.Sell - ticker.Buy; // 获取 Tick 数据的买卖价差
    // 账户余额与当前持仓价值的差值的 0.5倍
    var diffAsset = (acc.Balance - (acc.Stocks * ticker.Sell)) / 2;
    var ratio = diffAsset / acc.Balance; // diffAsset / 账户余额
    LogStatus('ratio:', ratio, _D()); // 打印 ratio和当前时间
    if (Math.abs(ratio) < threshold) { // 如果 ratio的绝对值小于指定阈值
        return false; // 返回 false
    }
    if (ratio > 0) { // 如果 ratio大于 0
        var buyPrice = _N(ticker.Sell + spread, ZPrecision); // 计算下单价格
        var buyAmount = _N(diffAsset / buyPrice, XPrecision); // 计算下单量
        if (buyAmount < MinStock) { // 如果下单量小于最小交易量
            return false; // 返回 false
        }
        exchange.Buy(buyPrice, buyAmount, diffAsset, ratio); // 买入下单
    } else {
        var sellPrice = _N(ticker.Buy - spread, ZPrecision); // 计算下单价格
        var sellAmount = _N(-diffAsset / sellPrice, XPrecision); // 计算下单量
        if (sellAmount < MinStock) { // 如果下单量小于最小交易量
            return false; // 返回 false
        }
        exchange.Sell(sellPrice, sellAmount, diffAsset, ratio); // 卖出下单
    }
    return true; // 返回 true
}

// 主函数
function main() {
    // 过滤非重要信息
    SetErrorFilter("GetRecords:|GetOrders:|GetDepth:|GetAccount|:Buy|Sell|timeout");
    while (true) { // 轮询模式
        if (onTick()) { // 执行 onTick 函数
            CancelPendingOrders(); // 取消未成交的挂单
            Log(_C(exchange.GetAccount)); // 打印当前账户信息
        }
        Sleep(LoopInterval * 1000); // 休眠
    }
}