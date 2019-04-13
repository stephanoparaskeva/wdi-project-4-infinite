class Common {
  static checkChange(coin, time) {
    if(coin[time].price_change_pct >= 0) {
      return 'up'
    }
    return 'down'
  }
}

export default Common
