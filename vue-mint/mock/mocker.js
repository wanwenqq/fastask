const proxy = {
    'GET /api/user': { id: 1, username: 'anders', sex: 6 },
    'GET /api/user/list': [
      { id: 1, username: 'anders', sex: 6 },
      { id: 2, username: 'simon', sex: 6 }
    ],
    'POST /api/login/account': (req, res) => {
      const { password, username } = req.body
      if (password === '111' && username === '111') {
        return res.send({
          status: 'ok',
          code: 0,
          token: '123321',
          data: { id: 1, username: 'anders', sex: 6 }
        })
      } else {
        return res.send({ status: 'error', code: 403 })
      }
    },
    'DELETE /api/user/:id': (req, res) => {
      console.log('---->', req.body)
      console.log('---->', req.params.id)
      res.send({ status: 'ok', message: '删除成功！' })
    },


    'GET /api/swtc/getAlltickers':[
        {id:1,name:'swtc',des:'0.00123'},
        {id:2,name:'jcc',des:'0.123'},
        {id:3,name:'moac',des:'1.234'},
        {id:4,name:'更多',des:''}
    ]
  }
  
  module.exports = proxy